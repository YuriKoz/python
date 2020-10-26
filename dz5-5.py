with open("Homework_4.txt", "x", encoding="utf-8") as data:
    numbers = input("Введите числа, разделённые пробелами: \n")
    data.writelines(f"{numbers}")

with open("Homework_4.txt", "r", encoding="utf-8") as data2:
    for num in data2:
        print(f"Сумма равна: {sum(int(i) for i in num.split())}")
