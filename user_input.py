def reverse(text):
    return text[::-1]

def is_palinrome(text):
    return text == reverse(text)

something = input('Введите текст: ')

something = something.lower()

forbidden = ('.','?','!',':',';','-','—',' ',)

for i in something:
    if i in forbidden:
        something = something.replace(i, '')
if(is_palinrome(something)):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')