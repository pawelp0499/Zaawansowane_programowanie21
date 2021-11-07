def modifying_list(list_1: list, list_2: list) -> list:
    return [i ** 3 for i in list(set(list_1 + list_2))]


print(modifying_list([1, 2, 3], [1, 0]))
