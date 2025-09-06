import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)

    if not abs_directory.startswith(abs_working_dir):
        f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
