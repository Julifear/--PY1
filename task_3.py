import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as out_f:
        data = out_f.readlines()
        data = [line.rstrip() for line in data]

    list_of_lists = [i.split(",") for i in data]

    headlines_list = list_of_lists[0]

    first_dict = dict([(headlines_list[i], list_of_lists[1][i]) for i in range(len(headlines_list))])
    second_dict = dict([(headlines_list[i], list_of_lists[2][i]) for i in range(len(headlines_list))])
    third_dict = dict([(headlines_list[i], list_of_lists[3][i]) for i in range(len(headlines_list))])
    forth_dict = dict([(headlines_list[i], list_of_lists[4][i]) for i in range(len(headlines_list))])

    list_dict = [first_dict, second_dict, third_dict, forth_dict]

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))