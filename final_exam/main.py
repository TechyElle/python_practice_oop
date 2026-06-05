import os
import sys
import importlib.util


def run_program(program_path: str) -> None:
    program_path = os.path.abspath(program_path)
    module_name = os.path.splitext(os.path.basename(program_path))[0]

    spec = importlib.util.spec_from_file_location(module_name, program_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load module")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <relative_path_to_script.py>")
        sys.exit(1)

    relative_path = sys.argv[1]
    run_program(relative_path)


if __name__ == "__main__":
    main()

