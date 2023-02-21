class A:
    def __init__(self, name):
        self.name = name

    def prints(self):
        print(f'меня зовут {self.name}')


class B:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Мне {self.age}'


class C(B):
    ...


class D(C):
    ...


class E(D, A):
    def __init__(self, name, age):
        D.__init__(self, age)
        A.__init__(self, name)


testing = E('Бегимай', 'ноль лет')
testing.prints()
print(testing)

import time

with open('gitcommands.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        time.sleep(1)
        print(i, end='')
