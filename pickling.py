import pickle

# имя файла, в котором мы сохраним обьект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')    # (бинарная запись)
pickle.dump(shoplist, f)    # помещаем обьект в файл    (консервируем)
f.close()

del shoplist    #   унечтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)     # загружаем обьект из файла     (разконсервируем)
print(storedlist)