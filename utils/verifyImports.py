import sys
from sys import *
from os import name, system

def clearScreen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def checkImports():
	try:
		import time
	except ImportError:
		while True:
			s = input("The module, 'time' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install time')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'time' found!")
		time.sleep(1)

	try:
		import os
	except ImportError:
		while True:
			s = input("The module, 'os' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install os')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'os' found!")
		time.sleep(1)

	try:
		import socket
	except ImportError:
		while True:
			s = input("The module, 'socket' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install socket')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'socket' found!")
		time.sleep(1)

	try:
		import sys
	except ImportError:
		while True:
			s = input("The module, 'sys' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install sys')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'sys' found!")
		time.sleep(1)

	try:
		import utils.calculatorBase as cb
	except ImportError:
		while True:
			s = input("The module, 'calculatorBase' was not found... This could be caused by an install error. Please restart the program and install a new Bear-Shell version. (hit y) ")
			if s == 'y':
				print("Quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'calculatorBase' found!")
		time.sleep(1)

	try:
		import ctypes
	except ImportError:
		while True:
			s = input("The module, 'ctypes' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install ctypes')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'ctypes' found!")
		time.sleep(1)

	try:
		import keyboard
	except ImportError:
		while True:
			s = input("The module, 'keyboard' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install keyboard')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'keyboard' found!")
		time.sleep(1)

	try:
		import psutil
	except ImportError:
		while True:
			s = input("The module, 'psutil' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install psutil')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'psutil' found!")
		time.sleep(1)

	try:
		import tkinter
	except ImportError:
		while True:
			s = input("The module, 'tkinter' was not found... Install? (y/n) ")
			if s == 'y':
				system('pip3 install tk')
				break
			elif s == 'n':
				print("Not installing, and quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable")
	else:
		print("Module, 'tkinter' found!")
		time.sleep(1)

	try:
		import utils.verifyImports
	except ImportError:
		while True:
			s = input("The module, 'calculatorBase' was not found... This could be caused by an install error. Please restart the program and install a new Bear-Shell version. (hit y) ")
			if s == 'y':
				print("Quitting the shell...")
				time.sleep(1)
				clearScreen()
				sys.exit()
			else:
				print("Not applicable!")

	else:
		print("Module, 'verifyImports' found!")
		time.sleep(1)
