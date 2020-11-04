def user_info(**kwargs):
    return kwargs


print(user_info(name=input("Введите Ваше имя: "), surname=input("Введите Вашу фамилию: "),
                birth_year=input("Введите год Вашего рождения: "),
                res_place=input("Введите город в котором Вы живёте: "), e_mail=input("Введите Ваш e-mail: "),
                tel_num=input("Введите Ваш номер телефона: ")))
