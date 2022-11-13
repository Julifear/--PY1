from random import choice


def get_unique_list_numbers() -> list:
    result = list()
    while len(result) < 15:
        i = choice([i for i in range(-10, 11)])
        if i not in result:
            result.append(i)
    return result


print(get_unique_list_numbers())
print(len(get_unique_list_numbers()) == len(set(get_unique_list_numbers())))