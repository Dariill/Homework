



grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]   # Исходные данные
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

results = {student: sum(grades)/len(grades)                                          # Словарь средний балл + Zip
          for student, grades in zip(sorted(students), grades)}

student_name = input("Name or all: ")                                                # Добавил консоль запроса

result = results.get(student_name, 'Not found')
print("avarge score " + str(student_name) + ": " + str(result))

if student_name =='all' :
    [print(results)]

