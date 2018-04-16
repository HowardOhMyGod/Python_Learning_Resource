class Employ:
    def __init__(self):
        self.name = 'Howard'
    @staticmethod
    def show_name(name):
        print(name)

    @property
    def email(self):
        return f'{self.name}@example.com'


    @email.setter
    def email(self, email):
        print('Set Email')
        self.name = email.split('@')[0]

class Teacher:
    def __init__(self, name='', class_name='', **kwargs):
        self.name = name
        self.cls_name = class_name

    def show(self):
        print(self.name, self.cls_name)


t1 = dict(name='Howard', class_name="Math", age=20)

teacher = Teacher(**t1)
teacher.show()


# Employ.show_name("Hi")
#
# e1 = Employ()
# print(e1.email)
# e1.email = 'Anna'
# print(e1.email)