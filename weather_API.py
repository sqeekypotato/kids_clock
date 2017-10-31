from weather import Weather
weather = Weather()

from settings import my_location

# class GetWeather:
#     print("getting weather")
#     lookup = weather.lookup_by_location(my_location)
#     forcasts = lookup.forecast()
#     todays_forcast = forcasts[0].text()
#     celcius = forcasts[0].high()
#     high_temp = int((int(celcius)-32)/1.8)

forcast_counter = 0

def forcast():
    print('getting weather')
    lookup = weather.lookup_by_location(my_location)
    forcasts = lookup.forecast()
    celcius = forcasts[0].high()
    high_temp = int((int(celcius)-32)/1.8)
    return (forcasts[0].text(), high_temp)


