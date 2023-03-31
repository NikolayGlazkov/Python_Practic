
def my_func(num1,num2,num3):
   
    array = [num1,num2,num3]
    
    array.sort()
    print(f"Сумма 2 наибольших чисел:",sum(array[1:3]))

num1 = int(input())
num2 = int(input())
num3 = int(input())

my_func(num1,num2,num3)