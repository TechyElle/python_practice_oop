import os
import sys
import importlib.util


def load_and_run(script_path: str) -> None:
    script_path = os.path.abspath(script_path)
    if not os.path.exists(script_path):
        raise FileNotFoundError(script_path)

    module_name = os.path.splitext(os.path.basename(script_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {script_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def main():
    if len(sys.argv) < 2:
        print("Usage: python final_exam_runner.py <absolute_or_relative_path_to_script.py>")
        sys.exit(1)

    load_and_run(sys.argv[1])


if __name__ == "__main__":
    main()

