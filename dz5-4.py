numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_numbers = []
new_words = []
file = open("Homework_3.txt", "r", encoding="utf-8")
content = file.read()
for i in content.split("\n"):
    for num in i:
        if num.isdigit():
            new_numbers.append(num)
    for num in i.split(" - "):
        if num not in new_numbers:
            new_words.append(num)

with open("Homework_7.txt", "w", encoding="utf-8") as data:
    keys, lis = [], 0
    for x in new_words:
        keys.append(numbers.get(x))
    for key in keys:
        print(key, "-", new_numbers[lis], file=data)
        lis += 1
