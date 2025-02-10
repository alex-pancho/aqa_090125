
def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
       які складаються з чисел, розділених комою."""
    result = []
    for i in string_list:
        try:
            result.append(sum([int(x) for x in i.split(",")]))
        except ValueError:
            result.append("Не можу це зробити!")

    return result

if __name__ == "__main__":
    output = sum_numbers_in_list(['1,2,3', '4,0,6'])
    print(output)
    
    output = sum_numbers_in_list(['1,2,3', '4/0,6', 'asas7,8,9'])
    print(output)