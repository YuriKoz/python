with open("Homework_2.txt", "r", encoding="utf-8") as data:
    salary = []
    low_salary = []
    for i in data:
        salary.append(float(i.split()[1]))
        if float(i.split()[1]) < 20000:
            low_salary.append(i.split()[0])
    print(f"Сотрудики имеющие оклад менее 20000: {', '.join(low_salary)}")
    print(f"Средняя величина дохода: {sum(salary) / len(salary)}")
