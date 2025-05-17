import sys
import requests
from pathlib import Path

curr_file_path = Path(__file__)
project_folder = curr_file_path.parent.parent
sys.path.append(str(project_folder))
# sys.path.append(str(project_folder / "lesson_15"))
# sys.path.append(str(project_folder / "lesson_16"))
from lesson_15 import lesson_15 as l15

# import lesson_16
print(sys.path)

car = l15.Car("lala", "tratata")
print(dir(car))
print(car.__dir__())
print(dir())
print(dir(__builtins__))

# from json import *
# v = loads(dumps('123'))
# print(v)
##############
# import json
# v = json.loads(json.dumps('123'))
# print(v)


# from json import (
#   loads,
#   'dict',
#   'dir',
#   'divmod',
#   )
def my_func():
    pass


__all__ = []

print(__file__)
print(l15.__name__)
