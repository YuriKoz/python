seasons = {"Зима.": (1, 2, 12), "Весна.": (3, 4, 5), "Лето.": (6, 7, 8), "Осень.": (9, 10, 11)}  # Только через словарь
months = int(input("Введите номер месяца от 1 до 12: "))
for key in seasons.keys():
    if months in seasons[key]:
        print(f"Этот месяц относится к сезону: {key}")

seasons = {"зима": [12, 1, 2], "весна": [3, 4, 5],  # Словарь и список
           "лето": [6, 7, 8], "осень": [9, 10, 11]}
month = int(input("Введите номер месяца от 1 до 12: "))
while month <= 0 or month > 12:
    month = int(input("Вы должны ввести число от 1 до 12. Введите число ещё раз: "))
for season, months in seasons.items():
    if month in months:
        print(f"{month}й месяц - это", season)

a = int(input('Введите номер месяца от 1 до 12: '))  # Вообще без списков и словарей
if a == 1 or a == 2 or a == 12:
    print('Это зима.')
elif a == 3 or a == 4 or a == 5:
    print('Это весна.')
elif a == 6 or a == 7 or a == 8:
    print('Это лето.')
elif a == 9 or a == 10 or a == 11:
    print('Это осень.')
else:
    print('Нет такого месяца.')






