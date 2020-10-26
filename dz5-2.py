file = open("Homework_1.txt", "r", encoding="utf-8")
lines = 0

for line in file.readlines():
    if line != "\n":
        lines += 1

file.seek(0)
counter = 0
content = file.read()
for line in content.split("\n"):
    counter += 1
    print(f"Колличество слов в {counter} строке: {len(line.split())}")

print(f"Количество строк в файле: {lines}")
