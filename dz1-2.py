print("Здравствуйте. Эта программа поможет Вам определить время по количеству секунд.")
time = int(input("Введите пожалуйста время в секундах: "))
seconds = time % 60
minutes = time % 3600 // 60
hours = time // 3600 % 24

print(f"На часах: {hours:02}:{minutes:02}:{seconds:02}")
