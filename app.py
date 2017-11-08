from flask import Flask, render_template, request, jsonify
from time import strftime
from settings import weather_symbols, weather_words, highlight_temperature
from weather_API import GetWeather

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def time():
    global counter, weather_result
    # handles weather
    if counter > 3600:
        weather_result.weather_call()
        counter = 0

    # handles time
    hour = strftime("%I")
    minutes = strftime("%M")
    tens = minutes[:1]
    ones = minutes[1:]
    other = strftime(" %p")

    # returns information to page on refresh
    if request.method == "POST":
        counter += 1
        print (counter)
        result = {'hour':hour, 'tens':tens, 'ones':ones, 'other':other,
                  'weather_symbol':weather_result.weather_symbol, 'temperature_scale':weather_result.temperature_scale,
                  'text':weather_result.weather_text}
        return jsonify(result)

    # provides information the first time the page loads
    return render_template('time.html', hour=hour, tens=tens, ones=ones, other=other,
                           weather_symbol=weather_result.weather_symbol, temperature_scale=weather_result.temperature_scale,
                           text=weather_result.weather_text)


if __name__ == "__main__":
    counter = 100
    weather_result = GetWeather()
    weather_result.weather_call()
    app.run()

