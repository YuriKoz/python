from sys import argv

name, development, rate, prize = argv
salory = int(development) * float(rate) + float(prize)
print(f"Зарплата составит : {salory:.2f}р.")
