# i)

def zad2_b_i(number_list: list) -> list:
    result = []
    for x in number_list:
        result.append(x * 2)
    return result
# ii)


def zad2_b_ii(number_list: list) -> list:
    return [i * 2 for i in number_list]


print(zad2_b_i([5, 10, 20, 30, 40]))
print(zad2_b_ii([1, 2, 3, 4, 5]))
