from flask import Flask, render_template, request, jsonify
from time import strftime
from settings import weather_symbols, weather_words, highlight_temperature
from weather_API import GetWeather

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def time():

    # handles weather
    weather = GetWeather()
    weather_text = weather.todays_forcast.lower()
    weather_symbol = weather_symbols[weather_words[weather_text]]
    temperature_scale = highlight_temperature(weather.high_temp)

    # handles time
    hour = strftime("%I")
    minutes = strftime("%M")
    tens = minutes[:1]
    ones = minutes[1:]
    other = strftime(" %p")

    # returns information to page
    if request.method == "POST":
        result = {'hour':hour, 'tens':tens, 'ones':ones, 'other':other,
                  'weather_symbol':weather_symbol, 'temperature_scale':temperature_scale}
        return jsonify(result)

    return render_template('time.html', hour=hour, tens=tens, ones=ones, other=other,
                           weather_symbol=weather_symbol, temperature_scale=temperature_scale)


@app.route('/testing', methods = ['GET'])
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host= '0.0.0.0')
