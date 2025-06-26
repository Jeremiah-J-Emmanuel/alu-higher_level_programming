#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util
    import sys

    # Load the compiled module from the .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Print all names in alphabetical order, excluding those starting with '__'
    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)
