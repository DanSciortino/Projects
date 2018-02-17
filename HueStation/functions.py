import random
import argparse
import textwrap


'''
Using arg parse to handle command line arguments
'''


def parseCommand():
	global debugFlag
	parse = argparse.ArgumentParser(prog='huestation.py',
	formatter_class=argparse.RawDescriptionHelpFormatter,
				description=textwrap.dedent('''\
				                   __ _        _   _            
				  /\  /\_   _  ___/ _\ |_ __ _| |_(_) ___  _ __  
				 / /_/ / | | |/ _ \ \| __/ _` | __| |/ _ \| '_ \ 
				/ __  /| |_| |  __/\ \ || (_| | |_| | (_) | | | |
				\/ /_/  \__,_|\___\__/\__\__,_|\__|_|\___/|_| |_|

				This application will read weather from dark sky
				And output it onto a hue light
				A debug mode is developed for testing
				This is used for testing certain color patterns
				

				Powered by Dark Sky
				'''))
	group = parse.add_mutually_exclusive_group(required=False)
	group.add_argument('-d',
						action='store_true',
	                    default=False,
	                    dest='flag',
	                    help="Enables Debugging mode with extra logging, also "
	                    "enables the end user to manually play a scene")

	group.add_argument('-r',
						action='store_true',
	                    default=False,
	                    dest='randomize',
	                    help='Randomize the color of the designated light for huestation')
	args = parse.parse_args()

	if(args.flag):
		import logging
		logging.basicConfig()
		return True

	elif(args.randomize):
		# randomize the state of the light
		b.set_light(output, 'hue', randint(1, 65535))
		b.set_light(output, 'sat', randint(1, 254))
		exit()


# Overloading the range function, Used for testing
# @param starting value, ending value, value to step by
# @return numbered range
def range(start, end, step):
	while start <= end:
		yield start
		start += step