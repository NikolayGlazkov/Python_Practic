def division (num1,num2):
    while True:
        try:
            if num2 == 0:
                print("Вы что? Пытаетесь делить на 0!")
            else:
                print(f"ответ :",num1 / num2)
                break
        except ValueError:
            print("Введите числа!")



num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

division(num1,num2)
