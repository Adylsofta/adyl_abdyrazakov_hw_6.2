class Person:
    def init(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_muself(self):
        print(f'{self.fullname} {self.age} {self.is_married}')


class Student(Person):
    def init(self, fullname, age, is_married, marks):
        super().init(fullname, age, is_married)
        self.marks = marks

    def average(self):
        b = sum(self.marks.values()) // len(self.marks)
        print(f'Student: {self.fullname}, {self.age} years, {self.is_married}, lesson: {self.marks}, average mark: {b}')


class Teacher(Student):
    def init(self, fullname, age, is_married, marks, experience, salary):
        super().init(fullname, age, is_married, marks)
        self.experience = experience
        self.salary = salary

    def salary1(self):
        if self.experience > 3:
            self.a = self.salary + (self.salary * 5 // 100 * self.experience)
            return self.a
        else:
            return self.salary

    def info(self):
        print(
            f'\nTeacher: {self.fullname} {self.age} years, {self.is_married}, {self.experience} year expirience, {self.a}\n')


teacher = Teacher('Jonh', 20, 'not married', {'biology': 10, 'chemistry': 4}, 6, 20000)
teacher.salary1()
teacher.info()


def create_student():
    st1 = Student('Nike', 18, 'not married', {'biology': 8, 'chemistry': 4})
    st2 = Student('Mary', 19, 'married', {'biology': 3, 'chemistry': 5})
    st3 = Student('Kris', 20, 'not married', {'biology': 9, 'chemistry': 1})

    lst = [st1, st2, st3]
    for i in lst:
        i.average()


create_student()