import json
from pathlib import Path

readme_path = Path(__file__).parent / "test_result.json"
print(readme_path)

with open(readme_path, 'r', encoding="utf8") as f:
    try:
        content = json.load(f)
    except json.decoder.JSONDecodeError:
        content = ""
    print(content)
    print(type(content))

json_string = '{"name": "John", "age": 30, "city": "New York", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'

json_to = json.loads(json_string)
print(json_to)
print(type(json_to))

# with open(readme_path, 'a', encoding="utf8") as f:
#     json.dump(json_to, f, indent=4)
"""
{

    "name": "John",
    "age": 30,
    "city": "New York"
}
"""