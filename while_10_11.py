
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0                                                   # новая переменная для индекса


while index < len(my_list):
    num = my_list[index]

    if num < 0:
        break                                               # стоп слово для цикла при встерче -5
    elif num == 0:
        index += 1                                          # комбо прибавил и присвоил
        continue
    print (num)
    index += 1                                              # функция while требует указателя для
                                                            # списка иначе она перебирает один и тот же индекс


# чтобы перебрать весь список можно использовать конструкцию "index += 1    continue" вместо "break"






