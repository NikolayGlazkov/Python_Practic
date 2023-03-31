kol = int(input("введите количество элементов в массиве: "))
array = []
for i in range(1,kol+1):
    array.append(int(input(f"введите число №{i} ")))

print(f"число X встречаеться",array.count(int(input("введите некоторое число X: "))))