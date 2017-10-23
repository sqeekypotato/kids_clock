
my_location = "Toronto"



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