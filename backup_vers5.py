import zipfile
import os
import time

# Выбор папки и название файла в который будет помещён архив
source = 'D:\shop s'

# Папка, которая будет заархивирована
target_dir = 'C:\Backup'

# Текущая дата, служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')

# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Имя zip-файла
target = today + os.sep + now + '.zip'

# Запрашиваем коментарий пойльзователя для имени файла
comment = input('Введите коментарий --> ')
if len(comment) == 0:   # Проверяем, введёт ли коментари
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'  # Замена пробелов на '_'
# Создаём каталог, если его еще нету
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
print('Каталог успешно создан', today)

# Создание архива в С - папке, с модификатором 'w' - замена файлов
z = zipfile.ZipFile(target, 'w')

# Список всех файлов и папок которые буду заархивированы
for root, dirs, files in os.walk(source):
    for file in files:
        z.write(os.path.join(root,file))    # Создание относительных путей и запись файлов в архив
if z != 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ!')
z.close()

