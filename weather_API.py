from weather import Weather
weather = Weather()

from settings import my_location

class GetWeather:
    lookup = weather.lookup_by_location(my_location)
    forcasts = lookup.forecast()
    todays_forcast = forcasts[0].text()
    celcius = forcasts[0].high()
    high_temp = int((int(celcius)-32)/1.8)

