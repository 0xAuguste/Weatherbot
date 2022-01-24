"""
Simple Python script to fetche weather data from:
<Open Weather Map> http://openweathermap.org/.
Based on script by Mohammad Laif at https://github.com/mzdhr/weather/blob/master/weather.py
City ID is for Albany, CA.
"""
import requests
import json
import datetime
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5322850&units=imperial&APPID=[INPUT_ID]')
r_json = r.json()
main = r_json.get('main')
sys = r_json.get('sys')
weather = r_json.get('weather')
data = dict(
	city=r_json.get('name'),
	country=sys.get('country'),
	temp=main.get('temp'),
	temp_max=main.get('temp_max'),
	temp_min=main.get('temp_min'),
	humidity=main.get('humidity'),
	pressure=main.get('pressure'),
	sky=r_json['weather'][0]['main'],
	condition=r_json['weather'][0]['description'],
	sunrise=sys.get('sunrise'),
	sunset=sys.get('sunset'),
	wind=r_json.get('wind').get('speed'),
	wind_deg=r_json.get('wind').get('deg'),
	dt=r_json.get('dt'),
	cloudiness=r_json.get('clouds').get('all'),
)
degree_sign= u'\N{DEGREE SIGN}'
#time_converter is currently broken. NameError: name 'time_converter' is not defined
def time_converter(time):
	"""
	Convert time from server format (unix timestamp), to readable human format.
	:param time: server unix timestamp.
	:return: readable human time format.
	"""
	converted_time = datetime.datetime.fromtimestamp(
		int(time)
	).strftime('%H:%M')
	return converted_time

def status():
	return (temperature() + degree_sign + " F and " + description() 
		+ ".\nWind is blowing " + degrees_to_bearings(data.get('wind_deg')) + " at " + wind() + " MPH.")

def sunStatus():
	return "The sun will rise at " + sunrise() + " a.m. and set at " + sunset() + " p.m."

def city():
	return data.get('city')

def description():
	return data.get('condition')

def temperature():
	return str(int(data.get('temp')))

def wind():
	return str(data.get('wind'))

def sunrise():
	rise = time_converter(data.get('sunrise'))
	if rise[0] == "0":
		rise = rise[1:]
	return rise

def sunset():
	sset = time_converter(data.get('sunset'))
	hours = int(sset[0:2])
	if hours > 12:
		hours = hours - 12
	return str(hours) + sset[2:]

def degrees_to_bearings(degrees):
	if degrees == 0 or degrees == 360:
		return "due East"
	elif degrees == 90:
		return "due North"
	elif degrees == 180:
		return "due West"
	elif degrees == 270:
		return "due South"
	elif degrees < 90:
		return "North " + str(int(90 - degrees)) + degree_sign + " East"
	elif degrees < 180:
		return "North " + str(int(degrees - 90)) + degree_sign + " West"
	elif degrees < 270:
		return "South " + str(int(270 - degrees)) + degree_sign + " West"
	else:
		return "South " + str(int(degrees - 270)) + degree_sign + " East"
