kol = int(input("введите количество элементов в массиве: "))
array = []
for i in range(1, kol+1):
    array.append(int(input(f"введите число №{i} ")))

max_value = max(array)
array.remove(max_value)

print(f"второй максимальный элимент это:", max(array))
