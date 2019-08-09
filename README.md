# Weather App Django
 
This is a Weather App developed with python and Django that inform us about climate in several cities.
This app can be runned in browsers.

<p align="center"><img src="https://github.com/Saul-Lara/Weather-App-Django/blob/master/image.jpg"/></p>

## Built With 🛠️
```
📄 Python
```

## Setup 🔧
Clone this 📁repository on your desktop.
In order to use the app, you need to obtain an 🌤[***OpenWeatherMap***](https://openweathermap.org/) API key and modify 📝`Weather App Django\WeatherApp\weather\views.py`.
```python
myApiKey = 'Add your openweathermap.org apy key here';
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + myApiKey
```
*Requires:* 
 - Python >= 2.7
 - Django >= 2.0
 - requests

## How to use? 💻
To run this project, you must perform these steps.

```
$ cd WeatherApp
$ python manage.py runserver
```

In the browser, you need type 127.0.0.1:8000 to view the 🌎 web application.



## License :page_facing_up: 
Code in this repository is open-sourced software licensed under the MIT license.
See the [LICENSE.md](https://github.com/Saul-Lara/Weather-App-Django/blob/master/LICENSE) file for details.

Saul Hdz Lara

---