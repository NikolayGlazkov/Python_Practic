def reverse_num(num):
    if num < 10:  # если число меньше 10 возврощаем его.
        return num
    else:
        last_digit = num % 10 #находим последнее число
        remaining_num = num // 10
        return int(str(last_digit) + str(reverse_num(remaining_num)))


num = int(input("Введите число :"))
print(reverse_num(num))
