from pathlib import Path
hack_user = input("user 2 hack: ")
person_of_hack = input("and you are: ")
file_path = Path("users")
full_path = file_path / f"{hack_user}.mgtgterminalgameuser"
with open (full_path, "r") as f:
    pwd = f.read()
print(pwd)