from colorama import init
from colorama import Fore, Back, Style

init()

#print(Style)
print(Fore.BLACK)
print(Back.GREEN)
what = input('Что ты хочешь сделать? (+, -): ')

# print(Style.BLACK)
print(Back.RED)
firstNum = float(input('Введите первое число: '))

#print(Style.BLACK)
print(Back.YELLOW)
secondNum = float(input('Введи второе число: '))

print(Back.WHITE)
if what == '+':
    result = firstNum + secondNum
    print('Результат: ' + str(result))
elif what == '-':
    result = firstNum - secondNum
    print('Результат: ' + str(result))
else:
    print('В этом *псевдо-калькуляторе* можно только + или - !!!')
