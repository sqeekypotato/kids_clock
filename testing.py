# import pyowm
# from api_key import API_KEY
#
# owm = pyowm.OWM(API_KEY)
# obsvtn = owm.daily_forecast('Toronto,CA')
# weather = obsvtn.get_weather()
#
# sky = weather._status
# current_temp = weather.get_temperature('celsius')['temp']
# high_temp = weather.get_temperature('celsius')['temp_max']
# print(current_temp)
# print (sky)
# print('hello')

from weather import Weather
weather = Weather()

def to_celcuis(temp):
    return int((int(temp)-32)/1.8)

lookup = weather.lookup_by_location("Toronto")


forcasts = lookup.forecast()
for i in forcasts:
    print(i.date(), i.text(), i.high())
