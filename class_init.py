class Person:
    def __init__(self, name):       # (self, name(Swaroop))
        self.anythingPeremennaya = name
    def sayHi(self):
        print('Привет! Меня зовут', self.anythingPeremennaya)

p = Person('Swaroop')
p.sayHi()

# Person('Swaroop').sayHi()

class SemerIsBoss:
    def __init__(self, doIt):
        self.semerdoIt = doIt
    def doU(self):
        print('Петрович!', self.semerdoIt + ' выходить?')

SemerIsBoss('Ты собираешься сегодня').doU()