def divide(a, b):
    # result = 0 # relocate to 7
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Помилка ділення на нуль: {e}")


def sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Do not use None here")
        return -1 # Nonsense

def divide_and_sum(a, b):
    # result = 0 # relocate to 7
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Помилка ділення на нуль: {e}")
        result = 0
    total_sum = sum(result, b)
    return total_sum


def key_proc(data_store):
    """Створимо ф-цю обробки - повернення  ліст по середині 
    або рандромне значення "середнього" ключа """
    if isinstance(data_store, list):
        list_len = len(data_store)
        index_of_element = int(list_len/2)
        try:
           return data_store[index_of_element]
        except IndexError:
            print("Empty list. Dont do it again!!!")
            # return None
    elif isinstance(data_store, dict):
        all_kyes = list(data_store.keys())
        dict_len = len(all_kyes)
        index_of_element = int(dict_len/2)
        try:
           key = all_kyes[index_of_element]
           return data_store[key]
        except IndexError: # (IndexError, KeyError)
            print("Empty dict. Dont do it again!!!")
        except KeyError:
            pass # наші дії 2
        except:
            pass # наші дії 3


# while True:
#     try:
#         print("*"* 88)
#    # except:  
#    #     pass


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль.")
    else:
        "Блок else виконується, якщо в блоку try не виникло жодного виключення"
        print(f"Результат ділення {a} на {b}: {result}")
    finally:
        # наприклад збереження в файл
        print("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")
    
# Магія продвинутого рівня
def key_proc_extend(data_store):
    """Створимо ф-цю обробки - повернення  ліст по середині 
    або рандромне значення "середнього" ключа"""
    if not isinstance(data_store, (list, dict)):
        raise ValueError("Ця функція лише для елітних лістів і діктів!")


def sum(a, b):
    try:
        result =  a + b
    except TypeError:
        print("Do not use None here")
        return -1 # Nonsense
    res = 1 + a
    return result, res


if __name__ == "__main__":
    a = 1
    b = None

    print(sum(a, b))
    print(divide_and_sum(10, 0))
    print(divide_and_sum(10, 2))     
    print("key_proc list", key_proc([1]))   
    print("key_proc", key_proc([1, 2]))
    print("key_proc", key_proc([1, 2, 3])) 
    print("key_proc", key_proc([]))
    print("key_proc DICT", key_proc({"a": 1}))
    print("key_proc", key_proc({"a": 1, "b": 2, "c": 3}))
    print("key_proc", key_proc({"a": 1, "b": 2, "c": 3, "f": 4, "g": 5}))
    print("key_proc", key_proc({}))
    try:
        # Код, який може викликати помилку читання з бази данних
        pass
    except InterruptedError:
        print("Помилка: данні не збереглися") 
    finally:
        # наприклад збереження в файл
        print("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")

    a = 1
    b = None
    print(sum(a, b))
    print("Go forward")
    print(sum(a, 1))

    # Приклад виклику функції
    divide_numbers(10, 2)
    divide_numbers(5, 0)
    try:
        key_after_proc = key_proc_extend("data_store") # key_proc("data_store")
    except ValueError as e:
        print("Fist print>", e)
        print("Ну ой.....")