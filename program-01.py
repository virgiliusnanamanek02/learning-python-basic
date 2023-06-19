def sum(a, b):
    return a + b


print(sum(2, 3))


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I'm " + self.name)


p = Person("John")
p.say_hello()
