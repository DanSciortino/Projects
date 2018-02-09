from time import sleep
import datetime
from random import *
import sys
import argparse
import textwrap

from phue import Bridge
from darksky import forecast

# Place holder before working on color transitions for 
# the weather dictionaries
x=1
# Different Dictionaries for all the
# weather patterns
clear = {'hue':0000,'sat':254, 'ct':154}
breezy = {'hue':33000,'sat':254}
partlyCloudy = {'hue':35000,'sat':x,'bri':84}
cloudy = {'hue':x,'sat':x}
sunny = {'hue':x,'sat':x}
lightRain = {'hue':x,'sat':x}
mediumRain = {'hue':x,'sat':x}
heavyRain = {'hue':x,'sat':x}
lightSnow = {'hue':x,'sat':x}
mediumSnow = {'hue':x,'sat':x}
heavySnow = {'hue':x,'sat':x}

# Define the output light
output = 7

# Overloading the range function, Used for testing
# @param starting value, ending value, value to step by
# @return numbered range
def range(start, end, step):
	while start <= end:
		yield start
		start += step

key = ''
hue = ''
ip = ''
longLat = 36.848889, -76.012381

b = Bridge(ip,hue)
parse = argparse.ArgumentParser(prog='huestation.py',
formatter_class=argparse.RawDescriptionHelpFormatter,description=textwrap.dedent('''\
			                   __ _        _   _            
			  /\  /\_   _  ___/ _\ |_ __ _| |_(_) ___  _ __  
			 / /_/ / | | |/ _ \ \| __/ _` | __| |/ _ \| '_ \ 
			/ __  /| |_| |  __/\ \ || (_| | |_| | (_) | | | |
			\/ /_/  \__,_|\___\__/\__\__,_|\__|_|\___/|_| |_|
			This application will read weather from dark sky api
			And output it onto a hue light
			A debug mode is developed for testing
			It will take the same name of the dictionary
			This is used for testing certain color patterns
			

			Powered by Dark Sky
			'''))
group = parse.add_mutually_exclusive_group(required=False)
group.add_argument('-d',
					action='store_true',
                    default=False,
                    dest='debugFlag',
                    help="Enables Debugging mode with extra logging, also "
                    "enables the end user to manually play a scene")

group.add_argument('-r',
					action='store_true',
                    default=False,
                    dest='randomize',
                    help='Randomize the color of the designated light for huestation') 
args = parse.parse_args()

if(args.debugFlag):
	import logging
	logging.basicConfig()
	print('debugs')

elif(args.randomize):
	# randomize the state of the light
	# b.set_light(output,'bri',randint(1,254))
	b.set_light(output,'hue',randint(1,65535))
	b.set_light(output,'sat',randint(1,254))
	exit()

# Checks to see if the time is between 9am and 8pm 
# else print a message
if(datetime.datetime.now().hour in range (9,20,1) or 
	args.debugFlag == True):
	with forecast(key, *longLat) as longLat:
		upcommingSummary = longLat.hourly[1].summary
		print(upcommingSummary)

		if(b.get_light(output,'on')== False):
			print('Turning light on\n')
			b.set_light(output,'on',True)
			b.set_light(output,'bri',127)

		if (upcommingSummary.find('Clear') != -1 or sys.argv[2] == 'clear'):
			b.set_light(output,'ct',clear['ct'],transitiontime=10)
		elif (upcommingSummary.find('Cloudy') != -1 or sys.argv[2] == 'cloudy'):	
			b.set_light(output,'bri',partlyCloudy['bri'],transitiontime=50)
			b.set_light(output,'hue',partlyCloudy['hue'],transitiontime=50)


		# for i in range(0,65535,1000):
		# 	b.set_light(output,'hue',i)
		# 	b.set_light(output,'sat',254)
		# 	print(i)
		# 	sleep(.3)  	
else:
	exit()

# Ranges
# hue 0...65535
# sat 0...254 
# ct  154...500
