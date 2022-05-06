import pyowm
#from pyowm import timestamps
from pyowm import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps

place = input("В каком городе: ")
owm = OWM('b6afb6109ec39d64c7829045fbb8fd74', language = "ru")
#mgr = owm.weather_manager()
observation = owm.weather_at_place(place)
w = observation.get_weather()
status = w.get_detailed_status()
print("В вашем городе " + place + " сейчас " + (status) )

#place = input("В каком городе: ")
# Search for current weather in London (Great Britain) and get details
#observation = owm.weather_at_place(place)
#w = observation.get_weather()
#print(w)


#owm = pyowm.OWM('0b9240d2be6d5cbf77a3f760c0e2c61c')

#place = input("В каком городе: ")
#observation = owm.weather_at_place(place)
#w = observation.weather
#print(w)
