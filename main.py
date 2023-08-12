import os

temp_dir = os.getenv('TMP')
temp_files = os.listdir(temp_dir)

for file in temp_files:
    if os.path.isfile(f'{temp_dir}\{str(file)}'):
        try:
            os.remove(f'{temp_dir}\{str(file)}')
        except PermissionError:
            continue
        except FileNotFoundError:
            continue
    elif os.path.isdir(f'{temp_dir}\{str(file)}'):
        dir_path = f'{temp_dir}\{str(file)}'
        dir_path_files = os.listdir(dir_path)
        try:
            for dir_file in dir_path_files:
                os.remove(f'{dir_path}\{dir_file}')
            os.rmdir(dir_path)
        except PermissionError:
            continue
        except FileNotFoundError:
            continue
