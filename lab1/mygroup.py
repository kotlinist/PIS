groupmates = [
    {"name": "Александр", "surname": "Иванов", "exams": ["Информатика", "ЭЭиС", "Web"], "marks": [4, 3, 5]},
    {"name": "Иван", "surname": "Петров", "exams": ["История", "АиГ", "КТП"], "marks": [4, 4, 4]},
    {"name": "Кирилл", "surname": "Смирнов", "exams": ["Философия", "ИС", "КТП"], "marks": [5, 5, 5]},

    {"name": "Мария", "surname": "Соколова", "exams": ["Математика", "Физика", "Химия"], "marks": [5, 4, 4]},
    {"name": "Елена", "surname": "Кузнецова", "exams": ["История", "Литература", "Обществознание"], "marks": [3, 4, 5]},
    {"name": "Дмитрий", "surname": "Волков", "exams": ["Информатика", "Математика", "Физика"], "marks": [5, 4, 4]},
    {"name": "Светлана", "surname": "Андреева", "exams": ["Web", "Базы данных", "Программирование"], "marks": [4, 4, 5]},
    {"name": "Олег", "surname": "Морозов", "exams": ["ИТ", "Математика", "Физика"], "marks": [3, 5, 5]},
    {"name": "Анастасия", "surname": "Григорьева", "exams": ["Химия", "Биология", "Математика"], "marks": [4, 4, 5]},
    {"name": "Виктор", "surname": "Егоров", "exams": ["История", "Право", "Обществознание"], "marks": [5, 4, 4]},
    {"name": "Наталья", "surname": "Попова", "exams": ["Философия", "Психология", "Социология"], "marks": [5, 5, 4]},
    {"name": "Сергей", "surname": "Крылов", "exams": ["Программирование", "Алгоритмы", "Структуры данных"], "marks": [5, 5, 5]},
    {"name": "Ирина", "surname": "Мельникова", "exams": ["Дизайн", "Менеджмент", "Маркетинг"], "marks": [4, 4, 3]},
    {"name": "Павел", "surname": "Никитин", "exams": ["Физика", "Математика", "Химия"], "marks": [4, 5, 5]},
    {"name": "Ольга", "surname": "Семенова", "exams": ["Литература", "История", "Обществознание"], "marks": [3, 4, 3]},
    {"name": "Юрий", "surname": "Беляев", "exams": ["ЭЭиС", "Информатика", "Математика"], "marks": [5, 4, 4]},
    {"name": "Евгения", "surname": "Васильева", "exams": ["Право", "География", "История"], "marks": [4, 4, 4]},
    {"name": "Максим", "surname": "Коновалов", "exams": ["Философия", "Психология", "КТП"], "marks": [3, 5, 4]},
    {"name": "Алина", "surname": "Федорова", "exams": ["КТП", "ИС", "Программирование"], "marks": [5, 4, 5]},
    {"name": "Владислав", "surname": "Захаров", "exams": ["История", "Обществознание", "Право"], "marks": [4, 3, 4]},
    {"name": "Татьяна", "surname": "Лебедева", "exams": ["Базы данных", "SQL", "Программирование"], "marks": [5, 5, 4]}
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))

def filter_students_by_average_mark(students, threshold):
    return [s for s in students if sum(s["marks"]) / len(s["marks"]) > threshold]

threshold_mark = float(input("Введите средний балл для фильтрации студентов: "))
filtered_students = filter_students_by_average_mark(groupmates, threshold_mark)
print_students(filtered_students)

