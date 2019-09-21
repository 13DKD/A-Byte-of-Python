from mymodule import sayHi, __version__

sayHi()
print('Версия', __version__)

# Так же можно
# from mymodule import *
# Однако не импортирует __version__, так как начинается с двойного __