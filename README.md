# Übersicht Weather Widget

Made for [Übersicht](http://tracesof.net/uebersicht/)

![the widget in action]
(https://raw.githubusercontent.com/nickroberts/dynamic-weather-widget/master/screenshot.png)

This is a weather widget based on the weather widget from https://github.com/felixhageloh/weather-widget

This also can be dynamic, based on your location (via your current ip address).

## Setup

You will need to edit some configurations in the `weather.py` file.

### Location

You can do one of 2 things:
1. Enter your latitude and longitude, along with your city and region code (state), making sure the dynamic section is commented out.
2. Uncomment the section for the dynamic location, making sure the section where you enter your latitude, longitude, city and region_code.

### Weather

Replace <api-key> with your own forecast.io api key.
You can get yours here: https://developer.forecast.io.

## Credits

Original widget by the Übersicht team:
https://github.com/felixhageloh/weather-widget

Icons by Erik Flowers:
http://erikflowers.github.io/weather-icons/
