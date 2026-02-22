import sys
from matrix_run.ui.terminal import show_cursor, hide_cursor
from matrix_run.ui.crt import get_crt_style, console

def prompt_input() -> str:
    show_cursor()
    
    sys.stdout.write("\n\033[1;32mneo>\033[0m ")
    sys.stdout.flush()
    try:
        user_msg = input()
    except EOFError:
        user_msg = "exit"
        
    hide_cursor()
    return user_msg

def render_stream(chunk: str):
    styled = get_crt_style(chunk, is_streaming=True)
    console.print(styled, end="")

def finish_stream():
    print()

def render_error(msg: str):
    print()
    err_text = get_crt_style(f"SYSTEM ERROR: {msg}\n", is_unstable=True)
    console.print(err_text, end="")
