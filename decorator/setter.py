class Employ:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.second)

    @property
    def email(self):
        return f'{self.first}.{self.second}@example.com'

    @fullname.setter
    def fullname(self, name):
        self.first, self.second = name.split(' ')



emp_1 = Employ("Howard", "Ho")

print(emp_1.fullname)

emp_1.first = 'Anna'

print(emp_1.email)

emp_1.fullname = "John Su"

print(emp_1.email)
print(emp_1.fullname)