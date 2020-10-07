a = 10
b = 1.3
sub_fname = "Павлик"
sub_lname = "Смирнов"

print(sub_fname + "у " + sub_lname + "у " + str(a) + " лет.")
print("В день он выпивает " + str(b) + " литра воды. \nПавлик - молодец.")

first_name = str(input("А как Вас зовут: "))
last_name = str(input("Какая у Вас фамилия: "))
age = int(input("Сколько Вам лет: "))
water_quant = float(input("Сколько воды в день вы пьёте: "))

print("Вас зовут " + first_name + ", а Ваша фамилия " + last_name + ".")
print("Вам " + str(age) + " лет. В день Вы выпиваете " + str(water_quant) + " литра воды.\nПохвально!")
