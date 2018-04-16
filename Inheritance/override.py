class TestBaseCls:
    def hello(self, name):
        print('Hello ', name)


class Tests(TestBaseCls):
    def hello(self):
        print('Hello Noname.')


t = Tests()
t.hello()
