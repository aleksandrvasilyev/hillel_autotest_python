from abc import ABC, abstractmethod
from random import randint
from faker import Faker


class SchoolStaff(ABC):

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    @abstractmethod
    def __str__(self):
        pass  # pass, потому что мы переопределяем метод __str__


class Teacher(SchoolStaff):
    def __str__(self):
        return f'Я учитель по имени {self.name} {self.surname}'

    def year_salary(self):
        return self.salary * 12


class TechnicalStaff(SchoolStaff):
    def __str__(self):
        return f'Я технический персонал по имени {self.name} {self.surname}'

    def fullname(self):
        return self.name + ' ' + self.surname


class School:
    def __init__(self, name, director, teachers, technicall_staffs):
        self.name = name
        self.director = director
        self.teachers = teachers
        self.technicall_staffs = technicall_staffs

    def new_director(self, director):
        self.teachers = [i for i in self.teachers if id(i) != id(director)] + [self.director]
        self.director = director


fake = Faker('ru')
ivan = Teacher('Ivan', 'Ivanov', randint(10000, 50000))
teachers = [Teacher(fake.first_name(), fake.last_name(), randint(10000, 50000)) for _ in range(5)]
tech_staffs = [TechnicalStaff(fake.first_name(), fake.last_name(), randint(10000, 50000)) for _ in range(5)]
school1 = School('169', ivan, teachers, tech_staffs)

for teacher in school1.teachers:
    print(teacher)

teachers_salary = sum([i.salary for i in school1.teachers])
techstaffs_salary = sum([i.salary for i in school1.technicall_staffs])
all_salaries = teachers_salary + techstaffs_salary
print(all_salaries)

new_teacher = Teacher(fake.first_name(), fake.last_name(), randint(10000, 50000))
school1.teachers += [new_teacher]
school1.new_director(new_teacher)
