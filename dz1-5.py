print("Здравствуйте, мы поможем Вам оценить деятельность Вашего предприятия.")
proceeds = float(input("Какова выручка предприятия в рублях?: "))
costs = float(input("Каковы издержки предприятия в рублях?: "))
profit = proceeds - costs
if proceeds > costs:
    print(f"Очень хорошо - Ваша организация вышла на прибыль. Она составила: {profit:.2f}р")
    employee_quant = int(input("Сколько сотрудников работает в Вашей организации?: "))
    emp_prof = profit / employee_quant
    print(f"В расчёте на одного сотрудника прибыль составит: {emp_prof:.2f}р")
elif proceeds == costs:
    print("Нужно потрудиться, Вы работаете в 0.")
else:
    print(f"Похоже у Вас не всё ладится - организация терпит убыток: {profit:.2f}р")
