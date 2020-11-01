start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
goal_list = [el for count, el in enumerate(start_list) if start_list[count] > start_list[count - 1]
             and count > 0]
print(goal_list)
