from os import *

def clearScreen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def blueScreen():
	clearScreen()
	print(f"""{bcolors.FAIL}
An critical error has been encountered!

Please restart Bear-Shell!
Error {bcolors.WARNING}471{bcolors.FAIL}: MEMORY_OVERLOAD

Causes:
	Spamming commands
	
{bcolors.HEADER}	""")