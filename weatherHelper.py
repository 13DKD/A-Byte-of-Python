import pyowm

owm = pyowm.OWM('7fc4d8bec164767d82678fa8a6bad33a', language = 'ru')

place = input('В каком городе/стране?: ')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']

print('В городе ' + place + ' сейчас - ' + w.get_detailed_status())
print('Температура сейчас в раёне ' + str(temp))

if temp < 10:
    print('Сейча дубарь, на улицу не ногой!!!')
elif temp < 20:
    print('Сейчас супер-мега-жесть как холодно, одовейся как танк!')
else:
    print('Температура норм, одевай что угодно')