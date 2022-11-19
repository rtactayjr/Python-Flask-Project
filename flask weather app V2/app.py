from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=API KEY HERE'
        response = requests.get(url.format(city_name)).json()
        
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        humid = response['main']['humidity']
        wind_speed = response['wind']['speed']
        icon = response['weather'][0]['icon']
        
        print(temp,weather,min_temp,max_temp,icon)
        return render_template('home.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name, humid=humid, wind_speed=wind_speed)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
