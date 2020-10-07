print("Здраствуйте, здесь можно узнать какая цифра в числе самая большая.")
number = int(input("Пожалуйста, введите целое положительное число: "))
max_value = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_value:
        max_value = number % 10
    number = number // 10
print("Самая большая цифра в числе: " + str(max_value))

