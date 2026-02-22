from dataclasses import dataclass
from typing import AsyncGenerator

@dataclass
class SSEEvent:
    event: str
    data: str

class SSEClient:
    def __init__(self, async_line_iterator):
        self.iterator = async_line_iterator
        
    async def events(self) -> AsyncGenerator[SSEEvent, None]:
        event_type = "message"
        data_buffer: list[str] = []
        
        async for raw_line in self.iterator:
            line = raw_line.rstrip('\r\n')
            if not line:
                if data_buffer:
                    yield SSEEvent(event=event_type, data="\n".join(data_buffer))
                event_type = "message"
                data_buffer = []
                continue
                
            if line.startswith(":"):
                continue
                
            if ":" in line:
                field, value = line.split(":", 1)
                value = value.lstrip(" ")
            else:
                field = line
                value = ""
                
            if field == "event":
                event_type = value
            elif field == "data":
                data_buffer.append(value)
        
        # Flush remaining data when stream ends without trailing blank line
        if data_buffer:
            yield SSEEvent(event=event_type, data="\n".join(data_buffer))
