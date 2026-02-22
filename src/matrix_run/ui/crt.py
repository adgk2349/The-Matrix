import random
from rich.console import Console
from rich.text import Text
from matrix_run.ui.terminal import hide_cursor, clear_screen, show_cursor, leave_alt_screen, enter_alt_screen

console = Console(highlight=False, markup=False)

# Global line counter for consistent scanline effect across streaming chunks
_line_counter = 0

def enter_fullscreen():
    hide_cursor()

def restore_terminal():
    show_cursor()
    leave_alt_screen()

def reset_line_counter():
    global _line_counter
    _line_counter = 0

def get_crt_style(text: str, is_unstable: bool = False, is_streaming: bool = False) -> Text:
    """Render text with CRT visual effects.
    
    Args:
        text: The text to style.
        is_unstable: Stronger effects for the 'signal unstable' phase.
        is_streaming: If True, disables glitch offset to prevent mid-word corruption.
    """
    global _line_counter
    result = Text()
    lines = text.split('\n')
    for i, line in enumerate(lines):
        flicker = random.random() < (0.05 if not is_unstable else 0.2)
        
        glitch_enabled = not is_streaming
        glitch = glitch_enabled and random.random() < (0.01 if not is_unstable else 0.05)
        
        # Use global counter for consistent scanline pattern across chunks
        style = "green"
        if flicker:
            style = "green dim"
        elif (_line_counter + i) % 2 == 0:
            style = "green bold"
            
        if glitch and line.strip():
            line = " " * random.randint(1, 3) + line
            
        result.append(line, style=style)
        if i < len(lines) - 1:
            result.append("\n")
    
    _line_counter += len(lines)
    return result
