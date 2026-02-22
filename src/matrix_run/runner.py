import getpass
from matrix_run import keychain
from matrix_run import prompts
from matrix_run.ui import splash, crt, chat, terminal
from matrix_run.llm import gemini_stream
from matrix_run.llm.types import GeminiAPIError

MAX_HISTORY = 20

async def main():
    terminal.setup()
    try:
        key = keychain.load()
        
        # Always show "Wake up, Neo..." sequence
        splash.short_unstable()
        
        if not key:
            terminal.show_cursor()
            while True:
                key = getpass.getpass("\033[1;32mGemini API Key (hidden): \033[0m")
                key = key.strip()
                if key:
                    break
                crt.console.print(
                    crt.get_crt_style("ERROR: Key cannot be empty. Try again.\n", is_unstable=True),
                    end=""
                )
            
            keychain.store(key)
        else:
            # Short stabilization message for returning users
            splash.short_stable()
        
        crt.enter_fullscreen()
        messages: list[dict] = [{"role": "system", "content": prompts.SYSTEM_PROMPT}]
        
        while True:
            try:
                crt.reset_line_counter()
                user_msg = chat.prompt_input()
                if not user_msg:
                    continue
                if user_msg.lower() in ["exit", "quit"]:
                    break
                
                messages.append({"role": "user", "content": user_msg})
                
                # Sliding window: keep system prompt + last N turns
                if len(messages) > MAX_HISTORY + 1:
                    messages = messages[:1] + messages[-(MAX_HISTORY):]
                
                content = ""
                async for chunk in gemini_stream.stream(messages, key):
                    chat.render_stream(chunk)
                    content += chunk
                
                chat.finish_stream()
                messages.append({"role": "assistant", "content": content})
                
            except KeyboardInterrupt:
                break
            except GeminiAPIError as e:
                chat.render_error(str(e))
                if messages and messages[-1]["role"] == "user":
                    messages.pop()
                continue
            except Exception as e:
                chat.render_error(f"Unexpected: {e}")
                if messages and messages[-1]["role"] == "user":
                    messages.pop()
                continue
    finally:
        crt.restore_terminal()
