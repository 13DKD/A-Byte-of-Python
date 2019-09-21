poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон - 
    используй Python!
'''

f = open('poem.txt', 'w')   # открываем для записи
f.write(poem)   # записываем текст в файл
f.close()   # закрываем файл

f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
    # режим чтения ('r' reading)

while True:
    line = f.readline()
    if len(line) == 0:  # нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close()   # закрываем файл

