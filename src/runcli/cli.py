import sys
import asyncio
from matrix_run.runner import main as run_matrix_main

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3 or sys.argv[1] != "matrix":
        print("Usage: run matrix [--reset]")
        sys.exit(1)
    
    reset_key = False
    if len(sys.argv) == 3:
        if sys.argv[2] in ["--reset", "--reset-key"]:
            reset_key = True
        else:
            print("Usage: run matrix [--reset]")
            sys.exit(1)
            
    try:
        if reset_key:
            from matrix_run.keychain import delete
            delete()
            print("Matrix API Key has been wiped from the system.")
            return

        asyncio.run(run_matrix_main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Matrix error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
