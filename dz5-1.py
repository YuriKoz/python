file1 = open("Homework.txt", "w", encoding="utf-8")

while True:
    inp = input("Введите несколько слов, для окончания ввода оставьте строку пустой: \n")
    file1.write(inp + "\n")
    if inp == "":
        break

file1.close()

