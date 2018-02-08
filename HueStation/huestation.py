from darksky import forecast
import datetime
from phue import Bridge
from time import sleep
from random import *
import sys

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

def main():
	debugflag = False
	key = ''
	hue = ''
	ip = '192.168.1.139'
	longLat = 36.848889, -76.012381

	b = Bridge(ip,hue)

	if(len(sys.argv) > 1):
		if(sys.argv[1] == '-d'):
			import logging
			logging.basicConfig()
			debugflag = True
			print(sys.argv[2])
			print('debugs')

		elif(sys.argv[1] == '-r'):
			# randomize the state of the light
			# b.set_light(output,'bri',randint(1,254))
			b.set_light(output,'hue',randint(1,65535))
			b.set_light(output,'sat',randint(1,254))

		elif(sys.argv[1] == '-i'):
			print("                   __ _        _   _             ")
			print("  /\  /\_   _  ___/ _\ |_ __ _| |_(_) ___  _ __  ")
			print("	/ /_/ / | | |/ _ \ \| __/ _` | __| |/ _ \| '_ \ ")
			print("/ __  /| |_| |  __/\ \ || (_| | |_| | (_) | | | |")
			print("\/ /_/  \__,_|\___\__/\__\__,_|\__|_|\___/|_| |_|")                           
			print('This application will read weather from dark sky api')
			print('And output it onto a hue light\n')
			print('A debug mode is developed for testing')
			print('It will take the same name of the dictionary')
			print('This is used for tetsing certain color patterns')
			print('\n\n\nPowered by Dark Sky')

	# Checks to see if the time is between 9am and 8pm 
	# else print a message
	if(datetime.datetime.now().hour in range (9,20,1) == True or debugflag == True):
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

if __name__ == "__main__":
	main() 
# Ranges
# hue 0...65535
# sat 0...254 
# ct  154...500