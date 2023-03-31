def sum_and_count(input_string, count=0,):
    """
    Функция принимает строку чисел, разделенных пробелами, и возвращает сумму чисел и количество чисел.
    """
    # базовый случай: если строка пустая, возвращаем результаты
    if input_string == "":
        return (0, count)

    # рекурсивный случай: находим первое число и рекурсивно вызываем функцию для оставшейся части строки
    first_space = input_string.find(" ")
    if first_space == -1:
        number = int(input_string)
        return (number, count+1)
    else:
        number = int(input_string[:first_space])
        remaining_string = input_string[first_space+1:]
        total, count = sum_and_count(remaining_string, count+1)
        return (number + total, count)

input_string = input()
print(sum_and_count(input_string, count=0))