number_list = [122, 125, 3, 9, 4, 0, 5, 0, 6, 0]

for index, number in enumerate(number_list):
    if index % 2 == 0:
        continue
    else:
        print(number)
