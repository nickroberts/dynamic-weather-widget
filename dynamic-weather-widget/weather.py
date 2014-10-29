# Import required libraries
import urllib2
import json

# Need the api key for forcast.io
apiKey   = '<api-key>'

# Comment the next 3 lines for dynamic weather based on your location via ip
location_string = '<latitude>,<longitude>'
exclude  = "minutely,hourly,alerts,flags"
location = "{ \"city\": \"<city>\", \"region_code\": \"<region-code>\" }"

# Get the location data based on ip
# Uncomment the next 3 lines for dynamic weather based on your location via ip
# location = urllib2.urlopen("http://freegeoip.net/json/").read()
# location_data = json.loads(location)
# location_string = str(location_data['latitude']) + ',' + str(location_data['longitude'])

# Get the weather
weather = urllib2.urlopen("https://api.forecast.io/forecast/" + apiKey + "/" + location_string + "?units=auto&exclude=" + exclude).read()
weather_data = json.loads(weather)

# Print the location and weather json
print "{ \"location\": " + location + ", \"weather\" : " + weather + " }"
