def read_file(file_path:str):
    """ Read file """
    content = None
    try:
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
    except FileNotFoundError:
        pass
    
    return content


if __name__ == "__main__":
    contain_in_file = read_file("anton.txt")
    print(contain_in_file)
    contain_in_file = read_file("C:\\Users\\opanchen\\aqa_090125\\lesson_07_bonus\\lesson_07_b.py")
    print(contain_in_file)