def numbers(num):
    if len(num) == 0:
        return (0, 0)
    else:
        # рекурсивный вызов для подстроки без последней цифры
        chet, nechet = numbers(num[:-1])
        if int(num[-1]) % 2 == 0:
            chet += 1
        else:
            nechet += 1
        # немогу понять как добавить в вывод строку перед значениями
        return (chet, nechet)


num = input("введите любои число :")
print(numbers(num))
