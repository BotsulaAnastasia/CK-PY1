def get_count_char(str_):
    str1 = str_.lower()
    dict_ = {
    }
    for letters in str1:
        if letters.isalpha():
            if letters in dict_:
                dict_[letters] += 1
            else:
                dict_[letters] = 1
    return dict_

    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_procent_char(str_):
    str2 = str_.lower()
    dict2 = {

    }
    for symbols in str2:
        if symbols in dict2:
            dict2[symbols] += 1
        else:
            dict2[symbols] = 1
    for values in dict2:
        dict2[values] /= sum(dict2.values())
    return dict2

print(get_procent_char(main_str))
