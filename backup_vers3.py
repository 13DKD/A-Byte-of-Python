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

# Создаём каталог, если его еще нету
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'

# Создание архива в С - папке, с модификатором 'w' - замена файлов
z = zipfile.ZipFile(target, 'w')

# Список всех файлов и папок которые буду заархивированы
for root, dirs, files in os.walk(source):
    for file in files:
        z.write(os.path.join(root,file))    # Создание относительных путей и запись файлов в архив
if z != 0:
    print('Резервная копия успешно создана в', z)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ!')
z.close()

