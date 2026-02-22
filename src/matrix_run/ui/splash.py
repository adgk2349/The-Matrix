import time
import sys
import random
from matrix_run.ui.crt import get_crt_style, console

def print_typing(text: str, delay: float = 0.08, is_unstable: bool = True):
    """Simulate human typing character by character."""
    for char in text:
        sys.stdout.write("\033[32m" + char + "\033[0m")
        sys.stdout.flush()
        # Add slight randomness to typing speed for realism
        time.sleep(delay + random.uniform(-0.02, 0.04))
    print()

def short_unstable():
    """First-run splash: the iconic movie intro."""
    console.clear()
    time.sleep(1) # Dramatic pause before starting
    
    # "Wake up, Neo..."
    print_typing("Wake up, Neo...", delay=0.15)
    time.sleep(2.5) # The matrix has you... comes after a pause
    
    # "The Matrix has you..."
    print_typing("The Matrix has you...", delay=0.12)
    time.sleep(2.5)
    
    # "Follow the white rabbit."
    print_typing("Follow the white rabbit.", delay=0.10)
    time.sleep(2)
    
    # "Knock, knock, Neo."
    print_typing("Knock, knock, Neo.", delay=0.08)
    time.sleep(1)
    
    # System transition log
    msg = "\nESTABLISHING CONNECTION..."
    console.print(get_crt_style(msg, is_unstable=True))
    time.sleep(0.5)

def short_stable():
    """Subsequent-run splash: signal stable, light CRT effects."""
    console.clear()
    msg = "\nCONNECTION ESTABLISHED."
    console.print(get_crt_style(msg, is_unstable=False))
    time.sleep(0.6)
