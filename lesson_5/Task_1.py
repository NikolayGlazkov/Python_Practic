def calculator():
    sign = input("Введите знак операции (+, -, *, /) или 0 для выхода: ")
    if sign == '0':
        return
    elif sign not in ['+', '-', '*', '/']:
        print("Ошибка: неверный знак операции")
        calculator()
        return
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if sign == '+':
        print("Ответ: ", num1 + num2)
    elif sign == '-':
        print("Ответ: ", num1 - num2)
    elif sign == '*':
        print("Ответ: ", num1 * num2)
    elif sign == '/':
        if num2 == 0:
            print("Ошибка: нельзя делить на ноль")
        else:
            print("Ответ: ", num1 / num2)
    calculator()

print(calculator())
