import datetime
from functions import *

from phue import Bridge
from darksky import forecast

conditions = ['heavy', 'light', 'rain', 'snow', 'sunny',
        'clear', 'partly', 'cloudy', 'breezy', 'overcast']
# Define the output light
hueOut = 7

'''
define the keys needed for the darksky api
the hue lights
the ip address of the hue bridge
and the longitude and the latitude
'''

key = 'af1fddaa8d0705f1a3d4be8e09464ab0'
hue = 'cS6LwGOCrzY0FJ6CqHNiQHZxm9yanIc7N1icvVet'
ip = '192.168.1.139'
longLat = 36.848889, -76.012381

debugFlag = parseCommand()

'''
Checks to see if the time is between 9am and 8pm or
if the debug flag has been raised
other wise do not run
'''
b = Bridge(ip, hue)

if(datetime.datetime.now().hour in range (9, 20, 1) or debugFlag):
	with forecast(key, *longLat) as longLat:
		
		'''
		Get the weather for the next hour and save it into a
		signal variable
		'''
		upcommingSummary = longLat.hourly[1].summary

		'''
		manipulate the encoding of the string from a unicode
		string to an ascii string and ignoring the u printed
		before each value in the list, also make all text lower case
		'''
		upcommingSummary = upcommingSummary.encode('ascii', 'ignore')
		upcommingSummary = upcommingSummary.lower()

		'''
		split the the lower case text into list and compare that
		newly created list agaisnt a known conditions list
		makes a new string with just the values from the conditions
		list
		'''
		weather = upcommingSummary.split()
		outputForecast = set(weather).intersection(conditions)
		weather = ' '.join(map(str, outputForecast))
		print(weather)

		'''
		check the status of the output light
		'''

		if(b.get_light(hueOut, 'on') == False):
			print('Turning light on\n')
			b.set_light(hueOut, 'on', True)
			b.set_light(hueOut, 'bri', 127)
		elif(b.get_light(hueOut, 'on') == True):
			print('Turning light off\n')
			b.set_light(hueOut, 'on', False)
			b.set_light(hueOut, 'on', True)


		def test(str):
			return{
				'clear':b.set_light(hueOut, 'ct', 154, transitiontime=10),
				'cloudy':(b.set_light(hueOut, 'bri', 84, transitiontime=20),
						b.set_light(hueOut, 'hue', 35000, transitiontime=20)),
			}.get(x)
else:
	exit()