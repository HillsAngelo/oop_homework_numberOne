import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_ex_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_ex_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() < other.get_avg_ex_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() > other.get_avg_ex_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() == other.get_avg_ex_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_ex_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_ex_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() < other.get_avg_ex_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() > other.get_avg_ex_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() == other.get_avg_ex_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def student_rank(students_list, course_name):
    ranked = []
    for student in students_list:
        for mark in student.grades[course_name]:
            ranked.append(mark)
            if len(ranked) == 0:
                return 'Ошибка'
        return f'Средняя оценка всех студентов на курсе {course_name} : {round(sum(ranked) / len(ranked), 2)}'


def lecturer_rank(lecture_list, course_name):
    ranked = []
    for lecturer in lecture_list:
        for mark in lecturer.grades[course_name]:
            ranked.append(mark)
            if len(ranked) == 0:
                return 'Ошибка'
        return f'Средняя оценка всех лекторов на курсе {course_name} : {round(sum(ranked) / len(ranked), 2)}'


best_student = Student('Evan', 'Miller', 'Male')
bad_student = Student('Vasya', 'Pupkin', 'Male')
bad_reviewer = Reviewer('Gordon', 'Ramsey')
cool_reviewer = Reviewer('Marat', 'Koliev')
cool_lecturer = Lecturer('Hideo', 'Kodjima')
bad_lecturer = Lecturer('Oleg', 'Tinkoff')

courses = ['Python', 'Git', 'Основы Python']

for i in [best_student, bad_student, cool_reviewer, bad_reviewer, cool_lecturer, bad_lecturer]:
    if isinstance(i, Student):
        for c in courses[0:2]: i.courses_in_progress.append(c)
        i.finished_courses.append(courses[2])

    if isinstance(i, Reviewer):
        for c in courses: i.courses_attached.append(c)

    if isinstance(i, Lecturer):
        for c in courses: i.courses_attached.append(c)

for r in [cool_reviewer, bad_reviewer, cool_lecturer, bad_lecturer]:
    for s in [best_student, bad_student]:
        for c in ['Python', 'Git', 'Основы Python']:
            if isinstance(r, Reviewer):
                for i in range(3):
                    r.rate_hw(s, c, random.randrange(4, 11))

            if isinstance(r, Lecturer):
                for i in range(3):
                    s.rate_lect(r, c, random.randrange(5, 11))

print(best_student.grades,
      bad_student.grades,
      cool_lecturer.grades,
      bad_lecturer.grades,
      cool_reviewer,
      bad_reviewer,
      cool_lecturer,
      bad_reviewer,
      best_student,
      bad_student, sep="\n"
      )

student_list = [bad_student, best_student]
lecturer_list = [bad_lecturer, cool_lecturer]

print(student_rank(student_list, 'Git'),
      student_rank(student_list, 'Python'),
      lecturer_rank(lecturer_list, 'Git'),
      lecturer_rank(lecturer_list, 'Python'), sep="\n"
      )
