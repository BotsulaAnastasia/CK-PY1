def delete(list_, index=None):
    if index == None:
        index = len(list_) - 1
        list1 = list_[:index]
    else:
        list1 = list_[:index] + list_[index+1:len(list_)]
    return list1


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
""" НЕ СОВПАДАЕТ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ С КОММЕНТАРИЯМИ К LINES 15-17. Условие удаления последнего символа не выполнено, 
    так как ожидаемый результат при проверке другой."""