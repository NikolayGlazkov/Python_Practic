import random


def guess_number(num, attempt):

    if attempt == 0:
        print(f"Вы проиграли! Загаданное число было: {num}")
        return False

    guess = int(input("Введите число от 0 до 100: "))
    if guess > num:
        print("Загаданное число меньше.")
    elif guess < num:
        print("Загаданное число больше.")
    else:
        print("Вы угадали!")
        return True

    return guess_number(num, attempt-1)


# Тестирование
num = random.randint(0, 100)
attempt = 10
# print(f"Загаданное число: {num}")
guess_number(num, attempt)
