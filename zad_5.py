def is_part(arg1: list, arg2: int) -> bool:
    return True if arg2 in arg1 else False


print(is_part([1, 2, 3], 1))
print(is_part([1, 2, 3], 0))
