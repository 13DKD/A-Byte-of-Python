import zipfile
import os
import time

# Создание архива в С - папке, с модификатором 'w' - замена файлов
z = zipfile.ZipFile('C:\Backup' + time.strftime('\%Y%m%d%H%M%S') + '.zip', 'w')

# Список всех файлов и папок которые буду заархивированы
for root, dirs, files in os.walk('D:\shop s'):
    for file in files:
        z.write(os.path.join(root,file))    # Создание относительных путей и запись файлов в архив
if z != 0:
    print('Резервная копия успешно создана в', z)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ!')
z.close()

