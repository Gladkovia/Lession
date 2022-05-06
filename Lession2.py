import pyowm
from pyowm import OWM

place = input("В каком городе: ")
owm = OWM('b6afb6109ec39d64c7829045fbb8fd74', language = "ru")

observation = owm.weather_at_place(place)
w = observation.get_weather()
status = w.get_detailed_status()
temp = w.get_temperature('celsius')["temp"]
print("В вашем городе " + place + " сейчас " + status )
print("Температура в " + place + " ровна " + str(temp))

if temp < 5:
    print("Сейчас холодно, нужна шапка! " + str(temp))
elif temp < 20:
    print("Сейчас тепло! " + str(temp) )
else:
    print("Сейчас " + str(temp) + " на твое усмотрение")
