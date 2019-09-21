shoplist = ['яблоки',
            'манго',
            'морковь',
            'бананы']
name = 'swaroop'

# Операция индексирования
print('Элемент 0 - ', shoplist[0])  # apple
print('Элемент 1 - ', shoplist[1])  # mango
print('Элемент 2 - ', shoplist[2])  # morkov
print('Элемент 3 - ', shoplist[3])  # bananas
print('Элемент -1 - ', shoplist[-1])    # bananas
print('Элемент -2 - ', shoplist[-2])    # morkov
print('Символ 0 - ', name[0])   # s

# Вырезка из списка
print('Элементы с 1 по 3: ', shoplist[1:3]) # mango, morkov
print('Элементы с 2 до конца: ', shoplist[2:])  # morkov, bananas
print('Элементы с 1 по -1: ', shoplist[1:-1])   # mango, morkov
print('Элементы от начала до конца: ', shoplist[:]) # apple mango morkov bananas

# Вырезка из строки
print('Символы с 1 по 3: ', name[1:3])  # wa
print('Символы с 2 до конца: ', name[2:])   # aroop
print('Символы с 1 по -1: ', name[1:-1])    # waroo
print('Символы от начала до конца: ', name[:])  # swaroop

# Вырезка с шагом
print('', shoplist[::1])    # all
print('', shoplist[::2])    # 0,2
print('', shoplist[::3])    # 0,3
print('', shoplist[::-1])   # all(but reverse)