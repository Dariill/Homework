immutable_var = (1, 'Tommyk', True, 5.13)
print('Исходный кортеж: ', immutable_var)            #Вывод на экран

try:
    immutable_var[0] = 2                             #Кортеж круглые скобки не изменяет
except TypeError as a:
    print ("АШИБКА: " , a)
    print('Кутёж нельзя менять, нажмите ALT + F4, помните это неизменяемый тип данных')

mutable_list = [1, 'Sobaks', False, 2.505]           #Список квадратные скобки изменьщик!!! Изменяется по индексу
print ("Исходный список: ", mutable_list)

mutable_list[0] = 500
mutable_list[1] = "Good Boy"                         #Важно соблюдение типа данных itr
print ("NEW список: ", mutable_list)


