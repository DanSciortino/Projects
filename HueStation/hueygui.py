'''
 HueyGui is based from tk_gui_complex.py from 
 studioimaginaire's example.  It has been modified
 to manipulate brightness, hue, and saturation
'''

from Tkinter import *
from phue import Bridge

hue = ''
ip = ''

b = Bridge(ip, hue)

'''
 Top level window properties
'''
root = Tk()
root.title('HueyGui')

'''
 Brigthness scale range 0...254
 	slider length of 500 pixels
 	single light assignment
'''
briScale = Scale(root, from_ = 254, to = 0,
				command = lambda x: 
				b.set_light(7, {'bri': int(x), 'transitiontime': 1}),
				label = 'Brightness',
				length = 500, showvalue = 1)

briScale.set(b.get_light(7,'bri'))
briScale.pack(padx = 10, pady = 40, side = LEFT)

'''
 Hue scale range 0...65535
 	slider length of 500 pixels
 	single light assignment
'''

hueScale = Scale(root, from_ = 65535, to = 0,
					command = lambda x:
					b.set_light(7, {'hue': int(x), 'transitiontime': 1}),
					label = 'Hue',
					length = 500, showvalue = 1)

hueScale.set(b.get_light(7,'hue'))
hueScale.pack(padx = 20, pady = 40, side = LEFT)

'''
 Saturation scale range 0...65535
 	slider length of 500 pixels
 	single light assignment
'''
satScale = Scale(root, from_ = 254, to = 0,
					command = lambda x:
					b.set_light(7, {'sat': int(x), 'transitiontime': 1}),
					label = 'Saturation',
					length = 500, showvalue = 1)

satScale.set(b.get_light(7,'sat'))
satScale.pack(padx = 40, pady = 40, side = LEFT)

'''
 Color Tempature scale range 500..154
 	slider length of 500 pixels
 	single light assignment
'''
ctScale = Scale(root,from_ = 500, to = 154,
					command = lambda x:
					b.set_light(7, {'ct': int(x), 'transitiontime': 1}),
					label = 'Color Temperature',
					length = 500, showvalue = 1)
ctScale.set(b.get_light(7,'ct'))
ctScale.pack(padx = 40, pady = 40, side = LEFT)

root.mainloop()