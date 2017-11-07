
my_location = "Toronto"

forcast_counter = 0

def highlight_temperature(temperature):
    temperature_scale = {
        'Hot': '.text-muted',
        'Warm': '.text-muted',
        'Cool': '.text-muted',
        'Cold': '.text-muted',
    }

    if temperature > 22:
        temperature_scale['Hot'] = 'text-danger'
    if 22 >= temperature > 12:
        temperature_scale['Warm'] = 'text-danger'
    if 12 >= temperature > 5:
        temperature_scale['Cool'] = 'text-danger'
    if temperature <= 5:
        temperature_scale['Cold'] = 'text-danger'

    return_value = '''
        <div class="col-xs-3 temperature weather" >
            <p><font class="{}"> Hot </font></p>
            <p><font class="{}"> Warm </font></p>
            <p><font class="{}"> Cool </font></p>
            <p><font class="{}"> Cold </font></p>
        </div>
    '''.format(temperature_scale['Hot'],temperature_scale['Warm'],temperature_scale['Cool'],temperature_scale['Cold'])
    return  return_value

weather_words = {
    "tornado": "thunderstorms",
    "tropical storm": "thunderstorms",
    "hurricane": "thunderstorms",
    "severe thunderstorms": "thunderstorms",
    "thunderstorms": "thunderstorms",
    "mixed rain and snow": "rain_snow",
    "mixed rain and sleet": "rain_snow",
    "mixed snow and sleet": "rain_snow",
    "freezing drizzle": "rain_snow",
    "drizzle": "rainy",
    "freezing rain": "rain_snow",
    "showers": "rainy",
    "snow flurries": "flurries",
    "light snow showers": "flurries",
    "blowing snow": "flurries",
    "snow": "flurries",
    "hail": "rainy",
    "sleet": "flurries",
    "dust": "cloudy",
    "foggy": "cloudy",
    "haze": "cloudy",
    "smoky": "cloudy",
    "blustery": "cloudy",
    "windy": "sunny",
    "cold": "sunny",
    "cloudy": "cloudy",
    "mostly cloudy (night)": "cloudy",
    "mostly cloudy (day)": "cloudy",
    "partly cloudy (night)": "sun_cloud",
    "partly cloudy (day)": "sun_cloud",
    "clear (night)": "sunny",
    "sunny": "sunny",
    "fair (night)": "sunny",
    "fair (day)": "sunny",
    "mixed rain and hail": "rainy",
    "hot": "sunny",
    "isolated thunderstorms": "thunderstorms",
    "scattered thunderstorms": "thunderstorms",
    "scattered showers": "sun_shower",
    "heavy snow": "flurries",
    "scattered snow showers": "flurries",
    "partly cloudy": "sun_cloud",
    "thundershowers": "thunderstorms",
    "snow showers": "flurries",
    "isolated thundershowers": "thunderstorms",
    "rain": "rainy",
    "breezy": "cloudy",
    'mostly cloudy':"sun_cloud",
}

weather_symbols = {

    "sun_shower":"""
        <div class="icon sun-shower">
            <div class="cloud"></div>
            <div class="sun">
                <div class="rays"></div>
            </div>
            <div class="rain"></div>
        </div>""",
    
    "thunderstorms":"""
        <div class="icon thunder-storm">
            <div class="cloud"></div>
            <div class="lightning">
                <div class="bolt"></div>
                <div class="bolt"></div>
            </div>
        </div>""",

    'cloudy':"""
        <div class="icon cloudy">
            <div class="cloud"></div>
            <div class="cloud"></div>
        </div>""",

    'flurries':"""
        <div class="icon flurries">
          <div class="cloud"></div>
          <div class="snow">
            <div class="flake"></div>
            <div class="flake"></div>
          </div>
        </div>""",

    'sunny':"""
        <div class="icon sunny">
          <div class="sun">
            <div class="rays"></div>
          </div>
        </div>""",

    'rainy':"""
        <div class="icon rainy">
          <div class="cloud"></div>
          <div class="rain"></div>
        </div>""",

    "sun_cloud":"""
        <div class="icon sun-shower">
            <div class="cloud"></div>
            <div class="sun">
                <div class="rays"></div>
            </div>
        </div>""",

    'rain_snow': """
    <div class="icon rainy">
      <div class="cloud"></div>
      <div class="rain"></div>
      <div class="flake"></div>
    </div>""",

}

if __name__ == '__main__':
    pass