import sys

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def enter_alt_screen():
    sys.stdout.write("\033[?1049h")
    sys.stdout.flush()

def leave_alt_screen():
    sys.stdout.write("\033[?1049l")
    sys.stdout.flush()

def setup():
    """Placeholder for any early terminal configuration."""
    pass
