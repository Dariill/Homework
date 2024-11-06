
my_dict = { "Tommyk": 1990, "Darii": 1985, "Coco Chanel": 1995}
print("Dict:", my_dict)


print("Existing value: ", my_dict["Tommyk"])                     # существующий ключ
print("Not existing value:", my_dict.get("Papich", "None"))   # отсутствующий ключ


my_dict["Papich"] = 1988                                             # Добавление данных
my_dict["Natan Drake"] = 1992
print("Update dictionary: ", my_dict)


removed_value = my_dict.pop("Papich")                                # Удаление данных
print("Deleted value: ", removed_value)

print("Modified dictionary: ", my_dict)


 # Sets

my_set = {1, "tommyk", True, 9.11, 1, "privet", False}
print("Set: ", my_set)                                               # повторы автоматически удалятся

                                                                     # Добавляем новые элементы
my_set.add("alarm")
my_set.add(2023)
print("Update set:", my_set)

                                                                     # Удаляем один элемент
my_set.remove("privet")
print("After deleted:", my_set)
