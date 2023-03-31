print("Ведите месяц года отсчте от 1 до 12")
array_time_of_ear = ["зима", "весна", "лето", "осень"]
manth_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    month = int(input())

    if month in manth_array[-1:]+manth_array[:2]:  # for winter
        print(array_time_of_ear[0])
        break

    elif month in manth_array[2:5]:  # for spring
        print(array_time_of_ear[1])
        break

    elif month in manth_array[4:8]:  # for summer
        print(array_time_of_ear[2])
        break

    elif month in manth_array[8:11]:  # for summer
        print(array_time_of_ear[3])
        break

    print("вы ввели не то ")
