from pathlib import Path

readme_path = Path(__file__).parent / "readme.txt"
print(readme_path)

with open(readme_path, 'r', encoding="utf8") as f:
    content = f.read()
    print(content)

with open(readme_path, 'w', encoding="utf8") as f:
    f.write('Hello, World!')


with open(readme_path, 'a', encoding="utf8") as f:
    f.write("\nДодав контент")
