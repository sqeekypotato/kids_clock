from weather import Weather

from settings import my_location, weather_words, weather_symbols, highlight_temperature
from error_logging import LogFile

class GetWeather:

    print("getting weather!")
    weather = Weather()
    lookup = ''
    forcasts = ''
    todays_forcast = ''
    fahrenheit = ''
    celcius = ''
    temperature_scale = ''
    weather_text = ''
    weather_symbol = ''

    def get_symbol(self, todays_forcast):
        # below figures out what symbol to display on the screen
        if todays_forcast in weather_words.keys():
            # tries to find the weather forecast in the list of symbols to display the correct icon
            weather_symbol = weather_symbols[weather_words[todays_forcast]]
        else:
            error_log = LogFile()
            error_log.logComment(' ')
            error_log.logComment('______________ new error log entry_________________')
            error_log.logComment(' ')
            error_log.logComment("""couldn't find {} in weather_words dict (look in settings.py),attempting to parse words""".format(todays_forcast))
            try:
                # if it couldn't find the word in the dict, then it tries to parse the word here
                sun_words = ['sun', 'sunny', 'clear']
                cloud_words = ['cloud', 'clouds', 'cloudy']
                rain_words = ['rain', 'rainy', 'shower', 'showers']
                thunderstorm_words = ['thunderstorms', 'thundershowers']
                found_word = False
                x = todays_forcast.split(" ")
                for word in x:
                    if word in sun_words:
                        weather_symbol = weather_symbols['sunny']
                        error_log.logComment('symbol set to sunny')
                        found_word = True
                    elif word in rain_words:
                        weather_symbol = weather_symbols['rainy']
                        error_log.logComment('symbol set to rainy')
                        found_word = True
                    elif word in thunderstorm_words:
                        weather_symbol = weather_symbols['thunderstorms']
                        error_log.logComment('symbol set to thunderstorms')
                        found_word = True
                    elif word in cloud_words:
                        weather_symbol = weather_symbols['cloudy']
                        error_log.logComment('symbol set to cloudy')
                        found_word = True
                if found_word == False:
                    weather_symbol = weather_symbols['sun_cloud']
                    error_log.logComment('parser had trouble with ' + todays_forcast)
                    error_log.logComment('symbol set to sun_cloud')
            except:
                error_log.logComment('****** parse failed settings symbol to default *******')
                # if all else fails, it just makes the symbol sun_cloud
                weather_symbol = weather_symbols['sun_cloud']
        return weather_symbol

    def weather_call(self):
        print('updating weather')
        self.lookup = self.weather.lookup_by_location(my_location)
        self.forcasts = self.lookup.forecast()
        self.todays_forcast = self.forcasts[0].text().lower()
        self.fahrenheit = self.forcasts[0].high()
        self.celcius = int((int(self.fahrenheit) - 32) / 1.8)
        self.temperature_scale = highlight_temperature(self.celcius)
        self.weather_text = self.todays_forcast + ' ' + str(self.celcius)
        self.weather_symbol = self.get_symbol(self.todays_forcast)



