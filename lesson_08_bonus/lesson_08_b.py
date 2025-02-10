
def read_file(file_path:str):
    """ Read file """
    file = None
    content = None
    try:
        # Відкриття файлу для читання
        file = open(file_path, "r", encoding="utf8")

        # Операції змістом файлу
        content = file.read()
    except Exception as e:  # Вловлювання помилки та збереження її у змінну e
        print(f"Виникла помилка: {e}")
    finally:
        # Закриття файлу у блоку finally, щоб гарантувати його виклик навіть якщо виникає помилка
        if file is not None:
            file.close()
    return content

def summm(a, b):
    return a + b

if __name__ == "__main__":
    contain_in_file = read_file("anton.txt")
    print(contain_in_file)
    contain_in_file = read_file("C:\\Users\\opanchen\\aqa_090125\\lesson_07_bonus\\lesson_07_b.py")
    print(contain_in_file)