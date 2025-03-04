from pathlib import Path, PurePosixPath

path_to_file_or_folder = Path("D:\\hillel\\aqa_090125\\lesson_13\\lesson.13.py")
print(path_to_file_or_folder)
path_linux = Path("~/hillel")
print(path_linux)

curr_file_path = Path(__file__)
print(curr_file_path)
print("Is file?", curr_file_path.is_file())
print("Is dir?", curr_file_path.is_dir())
print(f"{path_linux} exsist:", path_linux.exists())
print(curr_file_path.name)
print(path_to_file_or_folder.suffix)

lesson_13_folder_path = curr_file_path.parent
print("Is file?", lesson_13_folder_path.is_file())
print("Is dir?", lesson_13_folder_path.is_dir())
print(lesson_13_folder_path)
print(f"{lesson_13_folder_path} exsist:", lesson_13_folder_path.exists())

path_to_readme = lesson_13_folder_path / "readme.txt"
path_linux_readme = path_linux / "readme.txt"
print(path_to_readme)
print(PurePosixPath(path_linux_readme))
print(Path.cwd())
home_dir = Path.home()
print(home_dir)

project_folder = lesson_13_folder_path.parent
all_dirs = [d for d in project_folder.iterdir() if d.is_dir()]
print(all_dirs)
for dir in all_dirs:
    print(dir)

all_files = [f for f in project_folder.iterdir() if f.is_file()]
print(all_files)

extension = ".log"
all_log_files = [f for f in project_folder.iterdir() if f.suffix == extension]
print(all_log_files)
new_dir = lesson_13_folder_path / "homeworks" / "students"
new_dir.mkdir(parents=True, exist_ok=True)
shell = lesson_13_folder_path / "script.sh"
shell.mkdir(mode=0o777)
