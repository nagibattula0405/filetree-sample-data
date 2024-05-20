import sys

from Processor import __execute__


class Application:
    args_len = len(sys.argv)
    if args_len < 3:
        print("Example usage:")
        print("\n\tpython3 Processor.py <input_file_path> <output_file_path>")
        sys.exit(2)
    else:
        sys.exit(__execute__(sys.argv[1], sys.argv[2]))
