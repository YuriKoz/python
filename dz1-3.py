print("Здравствуйте, давайте попробуем подставить число в формулу: 'n + nn + nnn'")
number = int(input("Введите число: "))
summ = (str(number) + str(number+number) + str(number+number+number))
print("Ответ: " + summ)