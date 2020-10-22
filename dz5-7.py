import json
firms, revenue, costs, profit = [], [], [], []
data = []
with open("Homework_6.txt", "r", encoding="utf-8") as file:
    for i in file:
        firms.append(i.split()[0])
        revenue.append(i.split()[2])
        costs.append(i.split()[3])

    for num1, num2 in zip(revenue, costs):
        profit.append(int(num1) - int(num2))

    average = {"average": sum(i for i in profit if i > 0) /
               len([i for i in profit if i >= 0])}

    data_dict = dict(zip(firms, profit))
    data.append(data_dict), data.append(average)

with open("my_file.json", "w", encoding="utf-8") as write_f:
    json.dump(data, write_f)
