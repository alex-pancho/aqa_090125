while True:
    word = input("Введіть слово, яке містить літеру 'h' (або 'H'): ")
    if 'h' in word.lower(): 
        print("Дякуємо! Ви ввели слово з літерою 'h'.")
        break 
    else:
        print("У слові немає літери 'h'. Спробуйте ще раз.")