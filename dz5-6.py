dic = {}
values = []
keys = []
with open("Homework_5.txt", "r", encoding="utf-8") as f:
    for line in f:
        keys.append(line.split()[0])
        the_keys = line.split()[0]
        for key in the_keys.split():
            dic[key] = ''.join([i for i in line if i in '1234567890 '])
    for value in dic.values():
        values.append(sum(int(i) for i in value.split()))
    dictionary = dict(zip(keys, values))
    print(dictionary)
