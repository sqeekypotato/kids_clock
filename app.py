from flask import Flask, render_template, request, jsonify
from time import strftime
from settings import weather_symbols, weather_words
from weather_API import GetWeather

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def time():
    weather = GetWeather()
    weather_text = weather.todays_forcast.lower()
    weather_symbol = weather_symbols[weather_words[weather_text]]
    hour = strftime("%I")
    minutes = strftime("%M")
    tens = minutes[:1]
    ones = minutes[1:]
    other = strftime(" %p")
    if request.method == "POST":
        result = {'hour':hour, 'tens':tens, 'ones':ones, 'other':other}
        return jsonify(result)

    return render_template('time.html', hour=hour, tens=tens, ones=ones, other=other, weather_symbol=weather_symbol)


@app.route('/testing', methods = ['GET'])
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host= '0.0.0.0')
