from flask import Flask, render_template, request, jsonify
from time import strftime
from settings import weather_symbols, weather_words, highlight_temperature
from weather_API import forcast

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def time():

    # handles weather
    weather_result = forcast()
    weather_text = weather_result[0].lower()
    weather_symbol = weather_symbols[weather_words[weather_text]]
    temperature_scale = highlight_temperature(weather_result[1])

    # handles time
    hour = strftime("%I")
    minutes = strftime("%M")
    tens = minutes[:1]
    ones = minutes[1:]
    other = strftime(" %p")

    # returns information to page on refresh
    if request.method == "POST":
        result = {'hour':hour, 'tens':tens, 'ones':ones, 'other':other,
                  'weather_symbol':weather_symbol, 'temperature_scale':temperature_scale}
        return jsonify(result)

    # provides information the first time the page loads
    return render_template('time.html', hour=hour, tens=tens, ones=ones, other=other,
                           weather_symbol=weather_symbol, temperature_scale=temperature_scale)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host= '0.0.0.0')
