main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_count_char(str_):
    dict = {}
    for letter in str_.lower():
        if letter.isalpha():
            if not letter in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    return dict

dict = get_count_char(main_str)
print(dict)

def get_percent(dict):
    dict_perc = {}
    for value in dict:
        dict_perc[value] = round(dict[value] * 100 / sum(dict.values()), 2)
    return dict_perc
#print(get_percent(dict))