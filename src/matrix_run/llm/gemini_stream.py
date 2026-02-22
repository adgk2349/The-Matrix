import json
import httpx
from typing import AsyncGenerator
from .sse import SSEClient
from .types import GeminiAPIError

MODEL = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:streamGenerateContent?alt=sse"

async def stream(messages: list[dict], api_key: str) -> AsyncGenerator[str, None]:
    system_instruction = None
    contents = []
    
    for msg in messages:
        if msg["role"] == "system":
            system_instruction = {"parts": [{"text": msg["content"]}]}
        else:
            role = "model" if msg["role"] == "assistant" else "user"
            contents.append({"role": role, "parts": [{"text": msg["content"]}]})
    
    payload = {"contents": contents}
    if system_instruction:
        payload["systemInstruction"] = system_instruction

    headers = {"x-goog-api-key": api_key}
    timeout = httpx.Timeout(connect=10.0, read=120.0, write=10.0, pool=10.0)

    async with httpx.AsyncClient() as client:
        async with client.stream(
            "POST", API_URL, json=payload, headers=headers, timeout=timeout
        ) as response:
            if response.status_code != 200:
                body = await response.aread()
                raise GeminiAPIError(f"API Error {response.status_code}: {body.decode(errors='ignore')}")
                
            client_sse = SSEClient(response.aiter_lines())
            async for event in client_sse.events():
                if event.event == "error":
                    raise GeminiAPIError(event.data)
                if event.data:
                    try:
                        data = json.loads(event.data)
                        if "candidates" in data and len(data["candidates"]) > 0:
                            content = data["candidates"][0].get("content", {})
                            parts = content.get("parts", [])
                            for part in parts:
                                if "text" in part:
                                    yield part["text"]
                    except json.JSONDecodeError:
                        pass
