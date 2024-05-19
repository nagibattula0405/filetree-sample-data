import os


def validate_input_file_path(input_file_path: str):
    if not file_exist(input_file_path) or not file_readable(input_file_path) or not json_file(input_file_path):
        print("The input file either does not exist, is not readable, or does not end with .json")
        return False
    return True


def empty_input_file(input_file_path: str):
    if os.stat(input_file_path).st_size == 0:
        print(f"The input file [{input_file_path}] has no content")
        # System exit code can be 0 if empty file is allowed
        return True
    return False


def validate_output_file_path(output_file_path: str):
    if not file_exist(output_file_path) or not file_writable(output_file_path) or not json_file(output_file_path):
        print("The output file either does not exist, is not writable, or does not end with .json")
        return False
    return True


def file_exist(file_path: str):
    return os.path.isfile(file_path)


def file_readable(file_path: str):
    return os.access(file_path, os.R_OK)


def file_writable(file_path: str):
    return os.access(file_path, os.W_OK)


# Expecting the input file path will have a fully qualified filename with JSON extension,
# and if not, the check is not required
def json_file(file_path: str):
    return file_path.endswith('.json')


class Validator:
    pass
