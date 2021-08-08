from os import *

def blueScreen():
	if name == 'nt':
		system('color 1f')
	else:
		system('setterm -background blue -foreground white')
	print("""
An error has been encountered!

Please restart Bear-Shell!
Error 471: MEMORY_OVERLOAD
	""")