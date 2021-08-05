import sys
from sys import *
from os import name, system

missingImport = 0
bear_shell = "1.3.3"
bear_shell_testing = ""
testing = open('gitbranch.txt')
test = testing.read()

if test == 'true':
	bear_shell_testing = "(testing)"
else:
	bear_shell_testing = ""

def makeTest():
	f = open('gitbranch.txt', 'w')
	f.write("true")
	f.close()

def clearScreen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def writeVersionNum(ver):
	with open('data/version.data', 'w') as f:
		f.writelines(ver)

def startupVer():
	import os
	from dotenv import load_dotenv
	from github import Github
	load_dotenv()
	token = os.environ.get("api")
	g = Github(token)
	repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
	v = repo.get_contents("ver.txt")
	f = v.decoded_content
	if str(f) == "b'1.3.3'":
		print("Bear-Shell is up-to-date")
		time.sleep(1)
	else:
		print("Your Bear-Shell is out-of-date! Please consider updating!")
		print("This prompt will close in 10 seconds.")
		time.sleep(10)

import sys, time
try:
	from github import Github
except ImportError:
	clearScreen()
	while True:
		s = input("The module, 'PyGitHub' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install PyGitHub')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	clearScreen()
	print("Module, 'PyGitHub' found!")
	time.sleep(0.5)

try:
	import time
except ImportError:
	while True:
		s = input("The module, 'time' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install time')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'time' found!")
	time.sleep(0.5)

try:
	import os
except ImportError:
	while True:
		s = input("The module, 'os' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install os')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'os' found!")
	time.sleep(0.5)

try:
	import socket
except ImportError:
	while True:
		s = input("The module, 'socket' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install socket')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'socket' found!")
	time.sleep(0.5)

try:
	import sys
except ImportError:
	while True:
		s = input("The module, 'sys' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install sys')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'sys' found!")
	time.sleep(0.5)

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
	time.sleep(0.5)
try:
	import ctypes
except ImportError:
	while True:
		s = input("The module, 'ctypes' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install ctypes')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'ctypes' found!")
	time.sleep(0.5)

try:
	import keyboard
except ImportError:
	while True:
		s = input("The module, 'keyboard' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install keyboard')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'keyboard' found!")
	time.sleep(0.5)

try:
	import psutil
except ImportError:
	while True:
		s = input("The module, 'psutil' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install psutil')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'psutil' found!")
	time.sleep(0.5)

try:
	import tkinter
except ImportError:
	while True:
		s = input("The module, 'tkinter' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install tk')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'tkinter' found!")
	time.sleep(0.5)

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
	time.sleep(0.5)

try:
	from dotenv import load_dotenv
except ImportError:
	while True:
		s = input("The module, 'dotenv' was not found... Install? (y/n) ")
		if s == 'y':
			system('pip3 install python-dotenv')
			break
		elif s == 'n':
			print("Continuing startup...")
			missingImport += 1
			break
		else:
			print("Not applicable")
else:
	print("Module, 'dotenv' found!")
	time.sleep(0.5)
	startupVer()

def spinning_cursor():
	while True:
		for cursor in '|/-\\':
			yield cursor

spinner = spinning_cursor()

def clearScreen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
clearScreen()

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()
data_info = open('data/info.data')
data = data_info.read()

def slowPrint(s):
	f = str(s)
	for l in f:
		print(l, end="")
		time.sleep(.1)

# Utilities
def reset():
	print("Restarting...")
	time.sleep(1)
	os.system("python3 BearCMDos.py")

def error(message):
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
		
	print(f"{bcolors.FAIL}" + message)

def ramUsage():
	return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

def cpuUsage():
	return psutil.cpu_percent(interval=0.5)

def errorHandle(message, errorcode):
	mes = message
	err = errorcode
	print(f"{bcolors.FAIL}" + mes + " Error code: " + err)

class ErrorCodes:
	Err1 = "Syntax Error (Error Num: 0x0001)"
	Err2 = "Char not int (Error Num: 0x0002)"
	Err3 = "Not on list (Error Num: 0x0003)" 
	Err4 = "Illegal Operation (Error Num: 0x0004)"
	Err5 = "Not an accessable command (Error Num: 0x0005)"
	Err6 = "Not a valid directory (Error Num: 0x0006"
	ErrCode1 = "(Error Num: 0x00A1)"

class comFlags:
	yes = '-y'

#
# Setup Page
#
#
def setupPage():
	import os
	import time
	from os import system

	clearScreen()

	testing = open('gitbranch.txt')
	test = testing.read()


	with open('data/info.data', 'w') as f:
		f.writelines("1")

	print("Starting...")
	if missingImport > 0:
		print("Missing " + str(missingImport) + " libraries")
	else:
		print("All Libraries found!")
	for _ in range(30):
		sys.stdout.write(next(spinner))
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\b')
	clearScreen()

	if test == 'true':
		print("""
	Bear Shell v1.3.3 (testing)
	Bear Shell Registration
		""")
	else:
		print("""
	Bear Shell v1.3.3 (stable)
	Bear Shell Registration
		""")

	usrname = input("Please enter your new username: ")
	pas = input("Please enter your new password: ")

	with open('data/username.pass', 'w') as f:
		f.writelines(usrname)

	with open('data/password.pass', 'w') as f:
		f.writelines(pas)

	print("Registration Complete...")
	print("Opening Login...")
	time.sleep(0.5)
	loginPage()
#
# Login Page
#
def loginPage():
	import os
	import time
	import home as H
	from os import system

	clearScreen()

	print("Starting...")
	if missingImport > 0:
		print("Missing " + str(missingImport) + " libraries")
	else:
		print("All Libraries found!")
	for _ in range(30):
		sys.stdout.write(next(spinner))
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\b')
	clearScreen()

	testing = open('gitbranch.txt')
	test = testing.read()

	if test == 'true':
		print("""
	Bear Shell v1.3.3 (testing)
	Bear Shell Login
		""")
	else:
		print("""
	Bear Shell v1.3.3 (stable)
	Bear Shell Login
		""")

	while True:
		log = input("Enter Password To " + l_n + " To Login: ")

		if log == l_p:
			print("Opening Home Page...")
			time.sleep(0.5)
			clearScreen()
			homePage()
			break

		elif log == "559907":
			print("Developer Mode Activated...")
			time.sleep(0.5)
			clearScreen()
			devPage()
			break

		elif log == "559908":
			print("Taking you to root dev console...")
			time.sleep(0.5)
			clearScreen()
			devTermMain()
			break

		elif log == "bckgrnd":
			backgroundProcess()
			break

		elif log == "testing":
			testingTerm()
			break

		else:
			print("Wrong Passowrd To " + l_n)

def gameSelect():
		print(f"{bcolors.WARNING}Type command, 'exit' to leave")
		print(f"""{bcolors.OKBLUE}
		[1] Go to snake
		[2] [COMING SOON]
		[3] [COMING SOON]
		""")

		fff = input("[?]: ")

		if fff == '1':
			snakeDevGame()
		elif fff == '2':
			error("Game doesn't exist!")
		elif fff == '3':
			error("Game doesn't exist!")
		elif fff == 'exit':
			print("Going back to menu...")
			time.sleep(1)
			clearScreen()
			homePage()


		else:
			errorHandle("Game doesn't exist!", ErrorCodes.Err4)


def gameMenu():
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

	def gameSelect():
		print(f"{bcolors.WARNING}Type command, 'exit' to leave")
		print(f"""{bcolors.OKBLUE}
		[1] Go to snake
		[2] [COMING SOON]
		[3] [COMING SOON]
		""")

		fff = input("[?]: ")

		if fff == '1':
			snakeGame()
			clearScreen()
		elif fff == '2':
			error("Game doesn't exist!")
		elif fff == '3':
			error("Game doesn't exist!")
		elif fff == 'exit':
			print("Going back to menu...")
			time.sleep(1)
			clearScreen()
			homePage()

		else:
			errorHandle("Game doesn't exist!", ErrorCodes.Err4)
import home as H
import os
import time

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

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

def terminalMain():
	clearScreen()
	cwd = os.getcwd()
	print("Welcome to the Bear-Shell Terminal")
	print("Ver 1.3.3 " + bear_shell_testing)
	def helpCom():
		clearScreen()
		print("""
		Exit: Returns you to menu
		UserInfo: Tells you current user's information
		Root: Allows root terminal access
		python3: Allows you to run .py files
		clear: Clears screen
		ls: shows contents of given directory
		pwd: shows current directory
		restart: restarts the OS
		cd: allows you to access a directory
		cat: allows you to view the contents of a file
		git: allows you to run basic git commands
		(Linux Only!) neofetch: shows system info
		(Linux Only!) apt-get: allows you to run basic apt-get commands like: install, remove, update, and upgrade


		More commands to come with future updates:
		""")

	while True:
		bruhVariable = input(f"{bcolors.OKGREEN}Bear-Shell: " + f"{bcolors.OKBLUE}"+ cwd + " >>"f"{bcolors.OKGREEN} ")

		if bruhVariable == "Help":
			clearScreen()
			helpCom()
		elif bruhVariable == "help":
			clearScreen()
			helpCom()

		elif bruhVariable == "Exit":
			clearScreen()
			H.homePage()
			break
		elif bruhVariable == "exit":
			clearScreen()
			H.homePage()
			break

		elif bruhVariable == "UserInfo":
			clearScreen()
			b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
			if b_login == l_p:
				print("Username: " + l_n)
				print("Password: " + l_p)
			else:
				print("Wrong password")

		elif bruhVariable == "userinfo":
			clearScreen()
			b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
			if b_login == l_p:
				print("Username: " + l_n)
				print("Password: " + l_p)
			else:
				print("Wrong password")

		elif bruhVariable == "root":
			login = input("To access the root terminal, please enter your password: ")
			if login == l_p:
				dec = input(f"{bcolors.FAIL}Are you sure you want to enter the root terminal?{bcolors.HEADER} ")
				if dec == 'y':
					rootTerm()
				elif dec == 'Y':
					rootTerm()
				elif dec == 'n':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
				elif dec == 'N':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()

		elif bruhVariable == "Root":
			login = input("To access the root terminal, please enter your password: ")

			if login == l_p:
				dec = input("Are you sure you want to enter the root terminal? ")
				if dec == 'y':
					rootTerm()
				elif dec == 'Y':
					rootTerm()
				elif dec == 'n':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
					break
				elif dec == 'N':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
					break

			elif login != l_p:
				print("Wrong password!")

		elif bruhVariable == "clear":
			clearScreen()

		elif bruhVariable == "Clear":
			clearScreen()

		elif bruhVariable == "python3":
			m = input("What file would you like to run? ")
			if m.endswith('.py'):
				os.system(f'python3 {m}')
			else:
				print(m + " is not a py file.")

		elif bruhVariable == "ls":
			foo = input("What directory would you like to look through? ")
			isdir = os.path.isdir(foo)

			if isdir:
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + foo)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + foo)

			elif foo == 'ls':
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + cwd)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + cwd)

			else:
				errorHandle("That directory isn't valid!", ErrorCodes.Err6)

		elif bruhVariable == "pwd":
			print(cwd)

		elif bruhVariable == "restart":
			print("Restarting...")
			time.sleep(1)
			os.system("python3 BearCMDos.py")

		elif bruhVariable == "Restart":
			print("Restarting...")
			time.sleep(1)
			os.system("python3 BearCMDos.py")

		elif bruhVariable == "Pwd":
			print(cwd)

		elif bruhVariable == "cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

		elif bruhVariable == "Cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

			else:
				errorHandle("Directory doesn't exist!", ErrorCodes.Err6)

		elif bruhVariable == "neofetch":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				_ = system('neofetch')

		elif bruhVariable == "apt-get":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				while True:
					food = input("Would you like to run apt-get update, install, remove, or upgrade? ")
					if food == "update":
						print(f"{bcolors.WARNING}")
						system('sudo apt-get update')
						break

					elif food == "install":
						ding = input("What package do you want to install? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get install ' + ding)
						break
					
					elif food == "remove":
						fing = input("What package would you like to remove? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get remove ' + fing)
						break

					elif food == "upgrade":
						bing = input("Are you sure you want to upgrade? ")
						if bing == 'y':
							print(f"{bcolors.WARNING}")
							system('sudo apt-get dist-upgrade')

						else:
							print("Cancelling...")
							time.sleep(1)
							break
					
					else:
						print("Not an option!")

		elif bruhVariable == 'pip':
			while True:
				daisd = input("What pip package would you like to install? ")
				if daisd == 'exit':
					break
				else:
					os.system('pip3 install ' + daisd)
			
		elif bruhVariable == 'git':
			while True:
				bing = input("What git command would you like to run? (git init, git add, git commit, git branch, git remote add origin, or git push ('exit' to leave)) ")
				if bing == 'git init':
					system('git init')
				elif bing == 'git add':
					jaf = input("What files would you like to add? (* for all): ")
					system('git add ' + jaf)
				elif bing == 'git commit':
					fjd = input("What would you like the commit message to be? ")
					fling = f'"{fjd}"'
					system('git commit -m ' + fling)
				elif bing == 'git branch':
					sad = input("What branch do you want to use? ")
					system('git branch -M '+ sad)
				elif bing == 'git remote add origin':
					bva = input("What remote origin thing or whatever do you want to add? ")
					system('git remote add origin ' + bva)
				elif bing == 'git push':
					fja = input("What branch do you want to push too? ")
					system('git push -u ' + fja)
				elif bing == 'exit':
					print("Leaving git...")
					time.sleep(1)
					break

				else:
					errorHandle("Not a valid command! ", ErrorCodes.ErrCode1)
					print(f"{bcolors.WARNING}")

		elif bruhVariable == 'cat':
			faf = input("What file would you like to look into? ")
			if name == 'nt':
				
				_ = system('type ' + faf)
				print("\n")
			
			else:
				print(f"{bcolors.WARNING}")
				_ = system('cat ' + faf)
				print("\n")

		else:
			print("The command, " "'" + bruhVariable + "'" " wasn't found!")

def gameDevSelect():
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

	def error(message):
		clearScreen()
		print(f"{bcolors.FAIL}" + message)
		gameSelect()

	gameSelect()
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

def clearDumbScreen():
	clearScreen()

def error():
	clearScreen()
	print("This action doesn't exist, or hasn't been implemented yet.")
	homePage()

def homePage():
	incol = bcolors.OKGREEN
	login_pass = open('data/password.pass')
	login_name = open('data/username.pass')
	l_p = login_pass.read()
	l_n = login_name.read()
	testing = open('gitbranch.txt')
	test = testing.read()
	if test == 'true':
		print(f"""{bcolors.OKBLUE}
	Bear Shell v1.3.3 (testing)
	Home page

		""")
	else:
		print(f"""{bcolors.OKBLUE}
	Bear Shell v1.3.3 (stable)
	Home page

		""")
	print(f"{bcolors.OKBLUE}Welcome, " + l_n)
	print(f"{bcolors.OKBLUE}The Date Is: " + time.strftime("%m/%d/%y"))
	print(f"""{bcolors.OKBLUE}
	[1] To Open Google
	[2] To Open Text Editor
	[3] To Open File Explorer
	[4] To Configure and Open BioS
	[5] To Open Terminal
	[6] To Open Calculator
	[7] Show Recent Updates
	[8] To restart the system
	[9] To Close Shell Safely
	[10] To play games
	[11] To view system info
	[12] Check for Updates
	""")

	select = input(f"[?]:{incol} ")
	print(f"{bcolors.OKBLUE}")

	if select == '1':
		print("Called")
		error()

	elif select == '2':
		clearScreen()
		editorMain()

	elif select == '3':
		error()

	elif select == '4':
		clearScreen()
		testing = open('gitbranch.txt')
		test = testing.read()
		if test == 'true':
			gitf = "Testing"
		else:
			gitf = "Main"
		while True:
			b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
			if b_login == l_p:
				print("Opening BioS")
				print("Press enter the command 'e' to exit")
				host_name = socket.gethostname()
				host_ip = socket.gethostbyname(host_name)
				print("[1] USER NAME: " + l_n)
				print("[2] PASSWORD: " + l_p)
				print("[3] Current Repo Branch: " + gitf)
				print("Hostname:", host_name)
				print("LOCAL IPS: " + host_ip)
				edit_b = input("Enter [?] to change setting: ")
				if edit_b == '1':
					edit_n = input("Enter New Username: ")
					with open('data/username.pass', 'w') as f:
						f.writelines(edit_n)
					print("Username Changed To " + edit_n)
					input("Press Enter To Restart: ")
					homePage()
					os.system('exit')

				if edit_b == '2':
					edit_p = input("Enter New Password: ")
					with open('data/password.pass', 'w') as f:
						f.writelines(edit_p)

					print("Password Changed To " + edit_p)
					input("Press Enter To Restart: ")
					homePage()
					os.system('exit')

				if edit_b == '3':
					clearScreen()
					while True:
						if test == 'true':
							ax = input("Would you like to change to the main (stable) repo? ")
							a2 = ax.lower()
							if a2 == 'y':
								while True:
									asa = input("Are you sure you want to change back to the main branch? ")
									das = asa.lower()
									if das == 'y':
										#print("Now downgrading to the (stable) main branch...")
										#time.sleep(1)
										#system("cd ../")
										#system("rm -rf bear-shell")
										#system("git clone https://github.com/BizzyPythonBear/Bear-Shell/")
										#system("cd bear-shell")
										#system("python3 BearCMDos.py")
										#
										print("This command is a work in progress.")

									elif das == 'n':
										print("Returning to menu... ")
										time.sleep(0.5)
										clearScreen()
										homePage()
										break
										break
									else:
										print("Not an option.")
							elif a2 == 'n':
								print("Not changing to (main (stable)) branch...")
								print("Returning to menu...")
								time.sleep(0.5)
								clearScreen()
								homePage()
								break
							else:
								print("Not an option!")

						else:
							ax = input("Would you like to change to the testing (unstable) repo? ")
							a2 = ax.lower()
							if a2 == 'y':
								while True:
									asa = input("Are you sure you want to change to the testing branch? ")
									das = asa.lower()
									if das == 'y':
										pass
									elif das == 'n':
										print("Returning to menu... ")
										time.sleep(0.5)
										clearScreen()
										homePage()
										break
										break
									else:
										print("Not an option.")
							elif a2 == 'n':
								print("Not changing to (testing (unstable)) branch...")
								print("Returning to menu...")
								time.sleep(0.5)
								clearScreen()
								homePage()
								break
							else:
								print("Not an option!")

				if edit_b == 'E':
					clearScreen()
					print("Leaving BIOS...")
					time.sleep(0.5)
					homePage()
					break

				if edit_b == 'e':
					clearScreen()
					print("Leaving BIOS...")
					time.sleep(0.5)
					homePage()
					break

				else:
					print("You can't change that!")

			else:
				print("Wrong Password To " + l_n)

	elif select == '5':
		clearDumbScreen()
		terminalMain()

	elif select == '6':
		calculator()

	elif select == '7':
		clearDumbScreen()
		print(f"""
{bcolors.OKBLUE}Patch 1.3.3:
	{bcolors.OKGREEN}[+] Added Frame to start Github Branch Changing in BIOS
	{bcolors.OKGREEN}[+] Better Import verifier
	{bcolors.OKGREEN}[+] Missing Import Counter
	{bcolors.OKGREEN}[+] Github Branch Checker
	{bcolors.OKGREEN}[+] Added Frame to start Updater
		{bcolors.FAIL}[-] This Frame is causing lots of bugs! (BEWARE!)
	{bcolors.OKGREEN}[+] Fixed bug where bios would bring admins back to regular user menu
{bcolors.OKBLUE}Patch 1.3.2:
	{bcolors.OKGREEN}[+] Made commands able to type in uppercase and lowercase
	{bcolors.OKGREEN}[+] Version Checking
	{bcolors.OKGREEN}[+] Sys Info
{bcolors.OKBLUE}Update 1.3.1:
	{bcolors.OKGREEN}[+] Added the calculator
	{bcolors.OKGREEN}[+] Import Verification
	{bcolors.OKGREEN}[+] Expiremental Command Handling
{bcolors.OKBLUE}Update 1.3.1:
	{bcolors.OKGREEN}[+] Added 'pip' command
	{bcolors.OKGREEN}[+] Framework access; see developerGuide.txt for details
	{bcolors.OKGREEN}[+] Weird bug fix
{bcolors.OKBLUE}Patch 1.3.1:
	{bcolors.OKGREEN}[+] Fixed restarting; didn't actually restart the program
	{bcolors.OKGREEN}[+] Fixed DevPage bug where if command didn't exist it return user back to regular homepage instead of dev page
	{bcolors.OKGREEN}[+] Fixed small bugs
{bcolors.OKBLUE}Update 1.3.0:
	{bcolors.OKGREEN}[+] Git command added!
	  {bcolors.WARNING}-- More info inside terminal
{bcolors.OKBLUE}Update 1.2.9:
	{bcolors.OKGREEN}[+] apt-get command finally added! Usage: type 'apt-get' and say wether you want to install, remove, update, or upgrade
	{bcolors.OKGREEN}[+] cat command added; allows user to look into the contents of a file
{bcolors.OKBLUE}Update 1.2.8:
	{bcolors.OKGREEN}[+] Added the CD command
	{bcolors.OKGREEN}[+] Added the neofetch command
	{bcolors.OKGREEN}[+] Small cosmetic changes
{bcolors.OKBLUE}Update 1.2.7:
	{bcolors.OKGREEN}[+] Added 'ls' command; allows to look into directories
	{bcolors.OKGREEN}[+] Added 'pwd' command; allows to look at current directory
	{bcolors.OKGREEN}[+] Added 'restart' command; allows user to restart os from terminal
{bcolors.OKBLUE}Update 1.2.6:
	{bcolors.OKGREEN}[+] Added Command Prompt (Windows) compatability
{bcolors.OKBLUE}Update 1.2.5:
	{bcolors.OKGREEN}[+] More Error Codes
	{bcolors.OKGREEN}[+] Better Error Handler
	{bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 1.2.4:
	{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Terminal Based text editor soon!
	{bcolors.OKGREEN}[+] You can now run .py files from the terminal
{bcolors.OKBLUE}Update 1.2.3:
	{bcolors.OKGREEN}[+] Bug Fixes
	[+] Ability to Restart
	{bcolors.FAIL}[-] The browser feature wont be able to work for a while
{bcolors.OKBLUE}Update 1.2.2:
	{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Big Change with Menu Coming Soon!
	{bcolors.OKGREEN}[+] Cosmetics
	[+] Colors
		{bcolors.FAIL}[-] Not Enough Colors
	{bcolors.OKGREEN}[+] Minor Bug Fixes
{bcolors.OKBLUE}Update 1.2.1:
	{bcolors.OKGREEN}[+] Added Developer mode
	[+] Bug Fixes
	[+] Better Error Handling
{bcolors.OKBLUE}Update 0.2.1:
	{bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 0.0.1:
	{bcolors.OKGREEN}[+] Basic Files Added
		{bcolors.FAIL}[-] Lots Of Bugs
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Full github repository: {bcolors.OKGREEN}https://github.com/BizzyPythonBear/Bear-Shell-Unstable
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Legend:
{bcolors.OKGREEN}[+] is an Addition
{bcolors.FAIL}[-] is an issue created by the addition
{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Upcoming change/update
{bcolors.OKBLUE}--------------------------------------------
{bcolors.FAIL}Press 'e' to exit
		""")
		while True:
			thing = input("Command: ")
			if thing == 'e':
				clearScreen()
				homePage()
				break

			elif thing == 'E':
				clearScreen()
				homePage()
				break
			
			else:
				print("That isn't an 'e'.")

	elif select == '8':
		print("Restarting...")
		time.sleep(1)
		os.system("python3 BearCMDos.py")

	elif select == '9':
		print("Shutting down...")
		print("Have a nice day!")
		time.sleep(1)
		clearScreen()
		os.system('exit')
		sys.exit()
	
	elif select == '10':
		clearDumbScreen()
		gameSelect()

	elif select == '11':
		clearScreen()
		sysInfo()

	elif select == '12':
		from dotenv import load_dotenv
		from github import Github
		clearScreen()
		load_dotenv()
		token = os.environ.get("api")
		g = Github(token)
		repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
		print("Checking for updates...")
		v = repo.get_contents("ver.txt")
		f = v.decoded_content
		print("Current Github Repo Version: " + str(f))
		print("Checking if up-to-date...")
		time.sleep(1)
		if str(f) == "b'1.3.3'":
			clearScreen()
			print("You're up to date!")
			time.sleep(1)
			clearScreen()
			homePage()
		else:
			while True:
				d = input("You aren't up-to-date. Update? ")
				if d == 'n':
					print("Returning to menu...")
					time.sleep(1)
					clearScreen()
					homePage()
					break
				elif d == 'y':
					pass
				else:
					print("That isn't a command!")


	else:
		error()


def devPage():
	login_pass = open('data/password.pass')
	login_name = open('data/username.pass')
	l_p = login_pass.read()
	l_n = login_name.read()
	textColor = bcolors.OKGREEN
	if test == 'true':
		print(f"""{bcolors.OKBLUE}
	Bear Shell v1.3.3 (testing)
	Home page (DEVELOPER MODE: True)

		""")
	else:
		print(f"""{bcolors.OKBLUE}
	Bear Shell v1.3.3 (stable)
	Home page (DEVELOPER MODE: True)

		""")
	print(f"{bcolors.OKBLUE}Welcome, Admin")
	print(f"{bcolors.OKBLUE}The Date Is: " + time.strftime("%m/%d/%y"))
	print(f"""{bcolors.OKBLUE}
	[1] To Open Google
	[2] To Open Text Editor
	[3] To Open File Explorer
	[4] To Configure and Open BioS
	[5] To Open Terminal
	[6] To Open Calculator
	[7] To Show Recent Updates
	[8] To restart the system
	[9] To Close Shell Safely
	[10] To games
	[11] To Sys Info
	[12] Check for Updates
	""")

	select = input(f"[?]:{textColor} ")
	print(f"{bcolors.OKBLUE}")
	if select == '1':
		error()
		print(textColor)

	elif select == '2':
		clearScreen()
		devEditorMain()

	elif select == '3':
		error()

	elif select == '4':
		clearScreen()
		if test == 'true':
			gitf = "Testing"
		else:
			gitf = "Main"
		while True:
			print("Opening BioS")
			print("Press enter the command 'e' to exit")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("[3] Current Repo Branch: " + gitf)
			print("Hostname:", host_name)
			print("LOCAL IPS: " + host_ip)
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('data/username.pass', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				devPage()
				os.system('exit')

			if edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('data/password.pass', 'w') as f:
					f.writelines(edit_p)
				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				devPage()
				os.system('exit')

			if edit_b == '3':
				clearScreen()
				while True:
					if test == 'true':
						ax = input("Would you like to change to the main (stable) repo? ")
						a2 = ax.lower()
						if a2 == 'y':
							while True:
								asa = input("Are you sure you want to change back to the main branch? ")
								das = asa.lower()
								if das == 'y':
									print("This command is a work in progress.")
								elif das == 'n':
									print("Returning to menu... ")
									time.sleep(0.5)
									clearScreen()
									devPage()
									break
									break
								else:
									print("Not an option.")
						elif a2 == 'n':
							print("Not changing to (main (stable)) branch...")
							print("Returning to menu...")
							time.sleep(0.5)
							clearScreen()
							devPage()
							break
						else:
							print("Not an option!")
					else:
						ax = input("Would you like to change to the testing (unstable) repo? ")
						a2 = ax.lower()
						if a2 == 'y':
							while True:
								asa = input("Are you sure you want to change to the testing branch? ")
								das = asa.lower()
								if das == 'y':
									pass
								elif das == 'n':
									print("Returning to menu... ")
									time.sleep(0.5)
									clearScreen()
									devPage()
									break
									break
								else:
									print("Not an option.")
						elif a2 == 'n':
							print("Not changing to (testing (unstable)) branch...")
							print("Returning to menu...")
							time.sleep(0.5)
							clearScreen()
							devPage()
							break
						else:
							print("Not an option!")						

			if edit_b == 'E':
				clearScreen()
				print("Leaving BIOS...")
				time.sleep(0.5)
				devPage()
				break

			if edit_b == 'e':
				clearScreen()
				print("Leaving BIOS...")
				time.sleep(0.5)
				devPage()
				break

			else:
				print("You can't change that!")

	elif select == '5':
		clearScreen()
		devTermMain()

	elif select == '6':
		devCalculator()

	elif select == '7':
		clearScreen()
		print(f"""
{bcolors.OKBLUE}Patch 1.3.3:
	{bcolors.OKGREEN}[+] Added Frame to start Github Branch Changing in BIOS
	{bcolors.OKGREEN}[+] Better Import verifier
	{bcolors.OKGREEN}[+] Missing Import Counter
	{bcolors.OKGREEN}[+] Github Branch Checker
	{bcolors.OKGREEN}[+] Added Frame to start Updater
		{bcolors.FAIL}[-] This Frame is causing lots of bugs! (BEWARE!)
	{bcolors.OKGREEN}[+] Fixed bug where bios would bring admins back to regular user menu
{bcolors.OKBLUE}Patch 1.3.2:
	{bcolors.OKGREEN}[+] Made commands able to type in uppercase and lowercase
	{bcolors.OKGREEN}[+] Version Checking
	{bcolors.OKGREEN}[+] Sys Info
{bcolors.OKBLUE}Update 1.3.1:
	{bcolors.OKGREEN}[+] Added the calculator
	{bcolors.OKGREEN}[+] Import Verification
	{bcolors.OKGREEN}[+] Expiremental Command Handling
{bcolors.OKBLUE}Update 1.3.1:
	{bcolors.OKGREEN}[+] Added 'pip' command
	{bcolors.OKGREEN}[+] Framework access; see developerGuide.txt for details
	{bcolors.OKGREEN}[+] Weird bug fix
{bcolors.OKBLUE}Patch 1.3.1:
	{bcolors.OKGREEN}[+] Fixed restarting; didn't actually restart the program
	{bcolors.OKGREEN}[+] Fixed DevPage bug where if command didn't exist it return user back to regular homepage instead of dev page
	{bcolors.OKGREEN}[+] Fixed small bugs
{bcolors.OKBLUE}Update 1.3.0:
	{bcolors.OKGREEN}[+] Git command added!
	  {bcolors.WARNING}-- More info inside terminal
{bcolors.OKBLUE}Update 1.2.9:
	{bcolors.OKGREEN}[+] apt-get command finally added! Usage: type 'apt-get' and say wether you want to install, remove, update, or upgrade
	{bcolors.OKGREEN}[+] cat command added; allows user to look into the contents of a file
{bcolors.OKBLUE}Update 1.2.8:
	{bcolors.OKGREEN}[+] Added the CD command
	{bcolors.OKGREEN}[+] Added the neofetch command
	{bcolors.OKGREEN}[+] Small cosmetic changes
{bcolors.OKBLUE}Update 1.2.7:
	{bcolors.OKGREEN}[+] Added 'ls' command; allows to look into directories
	{bcolors.OKGREEN}[+] Added 'pwd' command; allows to look at current directory
	{bcolors.OKGREEN}[+] Added 'restart' command; allows user to restart os from terminal
{bcolors.OKBLUE}Update 1.2.6:
	{bcolors.OKGREEN}[+] Added Command Prompt (Windows) compatability
{bcolors.OKBLUE}Update 1.2.5:
	{bcolors.OKGREEN}[+] More Error Codes
	{bcolors.OKGREEN}[+] Better Error Handler
	{bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 1.2.4:
	{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Terminal Based text editor soon!
	{bcolors.OKGREEN}[+] You can now run .py files from the terminal
{bcolors.OKBLUE}Update 1.2.3:
	{bcolors.OKGREEN}[+] Bug Fixes
	[+] Ability to Restart
	{bcolors.FAIL}[-] The browser feature wont be able to work for a while
{bcolors.OKBLUE}Update 1.2.2:
	{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Big Change with Menu Coming Soon!
	{bcolors.OKGREEN}[+] Cosmetics
	[+] Colors
		{bcolors.FAIL}[-] Not Enough Colors
	{bcolors.OKGREEN}[+] Minor Bug Fixes
{bcolors.OKBLUE}Update 1.2.1:
	{bcolors.OKGREEN}[+] Added Developer mode
	[+] Bug Fixes
	[+] Better Error Handling
{bcolors.OKBLUE}Update 0.2.1:
	{bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 0.0.1:
	{bcolors.OKGREEN}[+] Basic Files Added
		{bcolors.FAIL}[-] Lots Of Bugs
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Full github repository: {bcolors.OKGREEN}https://github.com/BizzyPythonBear/Bear-Shell-Unstable
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Legend:
{bcolors.OKGREEN}[+] is an Addition
{bcolors.FAIL}[-] is an issue created by the addition
{bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Upcoming change/update
{bcolors.OKBLUE}--------------------------------------------
{bcolors.FAIL}Press 'e' to exit
		""")
		while True:
			thing = input("Command: ")
			if thing == 'e':
				clearScreen()
				devPage()
				break

			elif thing == 'E':
				clearScreen()
				devPage()
				break
			
			else:
				print("That isn't an 'e'.")

	elif select == '8':
		print("Restarting...")
		time.sleep(1)
		os.system("python3 BearCMDos.py")

	elif select == '9':
		print("Shutting down...")
		print("Have a nice day!")
		time.sleep(1)
		clearScreen()
		sys.exit()
	
	elif select == '10':
		clearScreen()
		gameDevSelect()

	elif select == '11':
		clearScreen()
		devSysInfo()
	
	elif select == '12':
		from dotenv import load_dotenv
		from github import Github
		clearScreen()
		load_dotenv()
		token = os.environ.get("api")
		g = Github(token)
		repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
		print("Checking for updates...")
		v = repo.get_contents("ver.txt")
		f = v.decoded_content
		print("Current Github Repo Version: " + str(f))
		print("Checking if up-to-date...")
		time.sleep(1)
		if str(f) == "b'1.3.3'":
			clearScreen()
			print("You're up to date!")
			time.sleep(1)
			clearScreen()
			homePage()
		else:
			while True:
				d = input("You aren't up-to-date. Update? ")
				if d == 'n':
					print("Returning to menu...")
					time.sleep(1)
					homePage()
					break
				elif d == 'y':
					pass
				else:
					print("That isn't a command!")

	else:
		clearScreen()
		errorHandle("Incorrect Command!", ErrorCodes.ErrCode1)
		devPage()

def snakeGame():
	import random
	import curses
	from curses import textpad
	import home as H

	OPPOSITE_DIRECTION_DICT = {
		curses.KEY_UP: curses.KEY_DOWN,
		curses.KEY_DOWN: curses.KEY_UP,
		curses.KEY_RIGHT: curses.KEY_LEFT,
		curses.KEY_LEFT: curses.KEY_RIGHT
	}

	DIRECTIONS_LIST = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]
	def create_food(snake, box):
		"""Simple function to find coordinates of food which is inside box and not on snake body"""
		food = None
		while food is None:
			food = [random.randint(box[0][0]+1, box[1][0]-1), 
			random.randint(box[0][1]+1, box[1][1]-1)]
			if food in snake:
				food = None
		return food
	def main(stdscr):
		# initial settings
		curses.curs_set(0)
		stdscr.nodelay(1)
		stdscr.timeout(100)
		# create a game box
		sh, sw = stdscr.getmaxyx()
		box = [[3,3], [sh-3, sw-3]]  # [[ul_y, ul_x], [dr_y, dr_x]]
		textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
		
		# create snake and set initial direction
		snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1]]
		direction = curses.KEY_RIGHT
		# draw snake
		for y,x in snake:
			stdscr.addstr(y, x, '#')
		# create food
		food = create_food(snake, box)
		stdscr.addstr(food[0], food[1], '*')
		# print score
		score = 0
		score_text = "Score: {}".format(score)
		stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
		while 1:
			# non-blocking input
			key = stdscr.getch()
				
			# set direction if user pressed any arrow key and that key is not opposite of current direction
			if key in DIRECTIONS_LIST and key != OPPOSITE_DIRECTION_DICT[direction]:
				direction = key
			# find next position of snake head
			head = snake[0]
			if direction == curses.KEY_RIGHT:
				new_head = [head[0], head[1]+1]
			elif direction == curses.KEY_LEFT:
				new_head = [head[0], head[1]-1]
			elif direction == curses.KEY_DOWN:
				new_head = [head[0]+1, head[1]]
			elif direction == curses.KEY_UP:
				new_head = [head[0]-1, head[1]]
			if curses.KEY_ENTER:
				homePage()
			# insert and print new head
			stdscr.addstr(new_head[0], new_head[1], '#')
			snake.insert(0, new_head)
			
			# if sanke head is on food
			if snake[0] == food:
				# update score
				score += 1
				score_text = "Score: {}".format(score)
				stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
				
				# create new food
				food = create_food(snake, box)
				stdscr.addstr(food[0], food[1], '*')
				# increase speed of game
				stdscr.timeout(100 - (len(snake)//3)%90)
			else:
				# shift snake's tail
				stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
				snake.pop()
			# conditions for game over
			if (snake[0][0] in [box[0][0], box[1][0]] or 
				snake[0][1] in [box[0][1], box[1][1]] or 
				snake[0] in snake[1:]):
				msg = "Game Over!"
				stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
				stdscr.nodelay(0)
				stdscr.getch()
				print("Final Score: " + str(score))
				break

	curses.wrapper(main)

def snakeDevGame():
	clearScreen()
	errorHandle("Game doesnt exist!", ErrorCodes.Err3)
	devPage()

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

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

def devTermMain():
	clearScreen()
	cwd = os.getcwd()
	print("Welcome to the Bear-Shell Terminal")
	print("Ver 1.3.3")
	print("(DEVELOPER MODE: ACTIVATED) (ROOT: TRUE)")
	def helpCom():
		clearScreen()
		print("""
		Exit: Returns you to menu
		UserInfo: Tells you current user's information
		python3: Allows you to run .py files
		clear: Clears screen
		ls: shows contents of given directory
		pwd: shows current directory
		restart: restarts OS
		cd: allows you to access a directory
		cat: allows you to view the contents of a file
		git: allows you to run basic git commands
		(Linux Only!) neofetch: sends system info
		(Linux Only!) apt-get: allows you to run basic apt-get commands like: install, remove, update, and upgrade

		More commands to come with future updates:
		""")

	while True:
		bruhVariable = input(f"{bcolors.OKGREEN}Bear-Shell: " + f"{bcolors.OKBLUE}"+ cwd + " >>"f"{bcolors.OKGREEN} ")

		pyfile = bruhVariable.endswith(".py")

		m = str(pyfile)

		if bruhVariable == "Help":
			clearScreen()
			helpCom()
		elif bruhVariable == "help":
			clearScreen()
			helpCom()

		elif bruhVariable == "Exit":
			clearScreen()
			devPage()
			break
		elif bruhVariable == "exit":
			clearScreen()
			devPage()
			break

		elif bruhVariable == "UserInfo":
			clearScreen()
			print("Username: " + l_n)
			print("Password: " + l_p)

		elif bruhVariable == "userinfo":
			clearScreen()
			print("Username: " + l_n)
			print("Password: " + l_p)

		elif bruhVariable == "clear":
			clearScreen()

		elif bruhVariable == "Clear":
			clearScreen()
		
		elif bruhVariable == "python3":
			m = input("What file would you like to run? ")
			if m.endswith('.py'):
				os.system(f'python3 {m}')
			else:
				print(m + " is not a py file.")

		elif bruhVariable == "restart":
			print("Restarting...")
			time.sleep(1)
			exec(open('BearCMDos.py').read())

		elif bruhVariable == "ls":
			foo = input("What directory would you like to look through? ")
			isdir = os.path.isdir(foo)

			if isdir:
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + foo)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + foo)

			elif foo == 'ls':
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + cwd)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + cwd)

			else:
				errorHandle("That directory isn't valid!", ErrorCodes.Err6)

		elif bruhVariable == "pwd":
			print(cwd)

		elif bruhVariable == "Restart":
			print("Restarting...")
			time.sleep(1)
			exec(open('BearCMDos.py').read())

		elif bruhVariable == "Pwd":
			print(cwd)

		elif bruhVariable == "cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

			else:
				print("Dir doesn't exist")

		elif bruhVariable == "Cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")
			else:
				print("Dir doesn't exist")

		elif bruhVariable == "neofetch":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				_ = system('neofetch')

		elif bruhVariable == "apt-get":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				while True:
					food = input("Would you like to run apt-get update, install, remove, or upgrade? ")
					if food == "update":
						print(f"{bcolors.WARNING}")
						system('sudo apt-get update')
						break

					elif food == "install":
						ding = input("What package do you want to install? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get install ' + ding)
						break
					
					elif food == "remove":
						fing = input("What package would you like to remove? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get remove ' + fing)
						break

					elif food == "upgrade":
						bing = input("Are you sure you want to upgrade? ")
						if bing == 'y':
							print(f"{bcolors.WARNING}")
							system('sudo apt-get dist-upgrade')

						else:
							print("Cancelling...")
							time.sleep(1)
							break
					
					else:
						print("Not an option!")

		elif bruhVariable == 'cat':
			faf = input("What file would you like to look into? ")
			if name == 'nt':
				
				_ = system('type ' + faf)
				print("\n")
			
			else:
				print(f"{bcolors.WARNING}")
				_ = system('cat ' + faf)
				print("\n")

		elif bruhVariable == 'git':
			while True:
				bing = input("What git command would you like to run? (git init, git add, git commit, git branch, git remote add origin, or git push ('exit' to leave)) ")
				if bing == 'git init':
					system('git init')
				elif bing == 'git add':
					jaf = input("What files would you like to add? (* for all): ")
					system('git add ' + jaf)
				elif bing == 'git commit':
					fjd = input("What would you like the commit message to be? ")
					fling = f'"{fjd}"'
					system('git commit -m ' + fling)
				elif bing == 'git branch':
					sad = input("What branch do you want to use? ")
					system('git branch -M '+ sad)
				elif bing == 'git remote add origin':
					bva = input("What remote origin thing or whatever do you want to add? ")
					system('git remote add origin ' + bva)
				elif bing == 'git push':
					fja = input("What branch do you want to push too? ")
					system('git push -u ' + fja)
				elif bing == 'exit':
					print("Leaving git...")
					time.sleep(1)
					break

				else:
					errorHandle("Not a valid command! ", ErrorCodes.ErrCode1)
					print(f"{bcolors.WARNING}")

		elif bruhVariable == 'pip':
			while True:
				daisd = input("What pip package would you like to install? ")
				if daisd == 'exit':
					break
				else:
					os.system('pip3 install ' + daisd)

		else:
			print("The command, " "" + bruhVariable + "" " wasn't found!")
import os
import home as H

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

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

def rootTerm():
	clearScreen()
	cwd = os.getcwd()
	print(f"{bcolors.OKCYAN}Welcome to the Bear-Shell Terminal")
	print("Ver 1.3.3")
	print("You're in the ROOT terminal, enter command 'exit' to return to menu.")
	def helpCom():
		clearScreen()
		print("""
		Exit: Returns you to menu
		UserInfo: Tells you current user's information
		python3: Allows you to run .py files
		clear: Clears screen
		ls: shows contents of given directory
		pwd: shows current directory
		restart: restarts OS
		cd: allows you to access a directory
		cat: allows you to view the contents of a file
		git: allows you to run basic git commands
		(Linux Only!) neofetch: sends system info
		(Linux Only!) apt-get: allows you to run basic apt-get commands like: install, remove, update, and upgrade

		More commands to come with future updates:
		""")

	while True:
		bruhVariable = input(f"{bcolors.OKGREEN}(ROOT) Bear-Shell: " + f"{bcolors.OKBLUE}"+ cwd + " >>"f"{bcolors.OKGREEN} ")
		print(f"{bcolors.OKCYAN}")
		if bruhVariable == "Help":
			clearScreen()
			helpCom()
		elif bruhVariable == "help":
			clearScreen()
			helpCom()

		elif bruhVariable == "Exit":
			clearScreen()
			H.homePage()
			break
		elif bruhVariable == "exit":
			clearScreen()
			H.homePage()
			break

		elif bruhVariable == "UserInfo":
			clearScreen()
			print("Username: " + l_n)
			print("Password: " + l_p)

		elif bruhVariable == "userinfo":
			clearScreen()
			print("Username: " + l_n)
			print("Password: " + l_p)

		elif bruhVariable == "python3":
			m = input("What file would you like to run? ")
			if m.endswith('.py'):
				os.system(f'python3 {m}')
			else:
				print(m + " is not a py file.")

		elif bruhVariable == "ls":
			foo = input("What directory would you like to look through? ")
			print(f"{bcolors.OKGREEN}")
			isdir = os.path.isdir(foo)
			if isdir:
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + foo)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + foo)
			else:
				errorHandle("That directory isn't valid!", ErrorCodes.Err6)

		elif bruhVariable == "pwd":
			print(cwd)

		elif bruhVariable == "restart":
			print("Restarting...")
			time.sleep(1)
			exec(open('BearCMDos.py').read())

		elif bruhVariable == "Restart":
			print("Restarting...")
			time.sleep(1)
			exec(open('BearCMDos.py').read())

		elif bruhVariable == "Pwd":
			print(cwd)
				
		elif bruhVariable == "Ls":
			foo = input("What directory would you like to look through? ")
			isdir = os.path.isdir(foo)
			if isdir:
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + foo)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + foo)
			else:
				errorHandle("That directory isn't valid!", ErrorCodes.Err6)

		elif bruhVariable == "cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

		elif bruhVariable == "Cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

		elif bruhVariable == "neofetch":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				_ = system('neofetch')

		elif bruhVariable == "apt-get":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				while True:
					food = input("Would you like to run apt-get update, install, remove, or upgrade? ")
					if food == "update":
						print(f"{bcolors.WARNING}")
						system('sudo apt-get update')
						break

					elif food == "install":
						ding = input("What package do you want to install? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get install ' + ding)
						break
					
					elif food == "remove":
						fing = input("What package would you like to remove? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get remove ' + fing)
						break

					elif food == "upgrade":
						bing = input("Are you sure you want to upgrade? ")
						if bing == 'y':
							print(f"{bcolors.WARNING}")
							system('sudo apt-get dist-upgrade')

						else:
							print("Cancelling...")
							time.sleep(1)
							break
					
					else:
						print("Not an option!")

		elif bruhVariable == 'cat':
			faf = input("What file would you like to look into? ")
			if name == 'nt':
				
				_ = system('type ' + faf)
				print("\n")
			
			else:
				print(f"{bcolors.WARNING}")
				_ = system('cat ' + faf)
				print("\n")

		elif bruhVariable == 'git':
			while True:
				bing = input("What git command would you like to run? (git init, git add, git commit, git branch, git remote add origin, or git push ('exit' to leave)) ")
				if bing == 'git init':
					system('git init')
					break
				elif bing == 'git add':
					jaf = input("What files would you like to add? (* for all): ")
					system('git add ' + jaf)
					break
				elif bing == 'git commit':
					fjd = input("What would you like the commit message to be? ")
					fling = f'"{fjd}"'
					system('git commit -m ' + fling)
					break
				elif bing == 'git branch':
					sad = input("What branch do you want to use? ")
					system('git branch -M '+ sad)
					break
				elif bing == 'git remote add origin':
					bva = input("What remote origin thing or whatever do you want to add? ")
					system('git remote add origin ' + bva)
					break
				elif bing == 'git push':
					fja = input("What branch do you want to push too? ")
					system('git push -u ' + fja)
					break
				elif bing == 'exit':
					print("Leaving git...")
					time.sleep(1)
					break

				else:
					errorHandle("Not a valid command! ", ErrorCodes.ErrCode1)
					print(f"{bcolors.WARNING}")

		elif bruhVariable == 'pip':
			while True:
				daisd = input("What pip package would you like to install? ")
				if daisd == 'exit':
					break
				else:
					os.system('pip3 install ' + daisd)

		else:
			print("The command, " "" + bruhVariable + "" " wasn't found!")

# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import home as H
# Defining TextEditor Class 
def editorMain():
	class TextEditor:
		# Defining Constructor
		def __init__(self,root):
			# Assigning root
			self.root = root
			# Title of the window
			self.root.title("Bork")
			# Window Geometry
			self.root.geometry("1200x700+200+150")
			# Initializing filename
			self.filename = None
			# Declaring Title variable
			self.title = StringVar()
			# Declaring Status variable
			self.status = StringVar()
			# Creating Titlebar
			self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
			# Packing Titlebar to root window
			self.titlebar.pack(side=TOP,fill=BOTH)
			# Calling Settitle Function
			self.settitle()
			# Creating Statusbar
			self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
			# Packing status bar to root window
			self.statusbar.pack(side=BOTTOM,fill=BOTH)
			# Initializing Status
			self.status.set("Welcome To Bork")
			# Creating Menubar
			self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
			# Configuring menubar on root window
			self.root.config(menu=self.menubar)
			# Creating File Menu
			self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding New file Command
			self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
			# Adding Open file Command
			self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
			# Adding Save File Command
			self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
			# Adding Save As file Command
			self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
			# Adding Seprator
			self.filemenu.add_separator()
			# Adding Exit window Command
			self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
			# Cascading filemenu to menubar
			self.menubar.add_cascade(label="File", menu=self.filemenu)
			# Creating Edit Menu
			self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding Cut text Command
			self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
			# Adding Copy text Command
			self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
			# Adding Paste text command
			self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
			# Adding Seprator
			self.editmenu.add_separator()
			# Adding Undo text Command
			self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
			# Cascading editmenu to menubar
			self.menubar.add_cascade(label="Edit", menu=self.editmenu)
			# Creating Help Menu
			self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding About Command
			self.helpmenu.add_command(label="About",command=self.infoabout)
			# Cascading helpmenu to menubar
			self.menubar.add_cascade(label="Help", menu=self.helpmenu)
			# Creating Scrollbar
			scrol_y = Scrollbar(self.root,orient=VERTICAL)
			# Creating Text Area
			self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
			# Packing scrollbar to root window
			scrol_y.pack(side=RIGHT,fill=Y)
			# Adding Scrollbar to text area
			scrol_y.config(command=self.txtarea.yview)
			# Packing Text Area to root window
			self.txtarea.pack(fill=BOTH,expand=1)
			# Calling shortcuts funtion
			self.shortcuts()
			# Defining settitle function
		def settitle(self):
			# Checking if Filename is not None
			if self.filename:
				# Updating Title as filename
				self.title.set(self.filename)
			else:
				# Updating Title as Untitled
				self.title.set("Untitled")
			# Defining New file Function
		def newfile(self,*args):
			# Clearing the Text Area
			self.txtarea.delete("1.0",END)
			# Updating filename as None
			self.filename = None
			# Calling settitle funtion
			self.settitle()
			# updating status
			self.status.set("New File Created")
			# Defining Open File Funtion
		def openfile(self,*args):
			# Exception handling
			try:
				# Asking for file to open
				self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
				# checking if filename not none
				if self.filename:
					# opening file in readmode
					infile = open(self.filename,"r")
					# Clearing text area
					self.txtarea.delete("1.0",END)
					# Inserting data Line by line into text area
				for line in infile:
					self.txtarea.insert(END,line)
				# Closing the file  
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Opened Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
			# Defining Save File Funtion
		def savefile(self,*args):
		# Exception handling
			try:
				# checking if filename not none
				if self.filename:
					# Reading the data from text area
					data = self.txtarea.get("1.0",END)
					# opening File in write mode
					outfile = open(self.filename,"w")
					# Writing Data into file
					outfile.write(data)
					# Closing File
					outfile.close()
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Saved Successfully")
				else:
					self.saveasfile()
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining Save As File Funtion
		def saveasfile(self,*args):
		# Exception handling
			try:
				# Asking for file name and type to save
				untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
				# Reading the data from text area
				data = self.txtarea.get("1.0",END)
				# opening File in write mode
				outfile = open(untitledfile,"w")
				# Writing Data into file
				outfile.write(data)
				# Closing File
				outfile.close()
				# Updating filename as Untitled
				self.filename = untitledfile
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Saved Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining Exit Funtion
		def exit(self,*args):
			op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
			if op>0:
				self.root.destroy()
				homePage()
			else:
				return
		# Defining Cut Funtion
		def cut(self,*args):
			self.txtarea.event_generate("<<Cut>>")
		# Defining Copy Funtion
		def copy(self,*args):
			self.txtarea.event_generate("<<Copy>>")
		# Defining Paste Funtion
		def paste(self,*args):
			self.txtarea.event_generate("<<Paste>>")
		# Defining Undo Funtion
		def undo(self,*args):
		# Exception handling
			try:
				# checking if filename not none
				if self.filename:
					# Clearing Text Area
					self.txtarea.delete("1.0",END)
					# opening File in read mode
					infile = open(self.filename,"r")
					# Inserting data Line by line into text area
					for line in infile:
						self.txtarea.insert(END,line)
					# Closing File
					infile.close()
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Undone Successfully")
				else:
					# Clearing Text Area
					self.txtarea.delete("1.0",END)
					# Updating filename as None
					self.filename = None
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Undone Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining About Funtion
		def infoabout(self):
			messagebox.showinfo("About Text Editor","Bork is a simple text editor included inside of Bear-Shell")
		# Defining shortcuts Funtion
		def shortcuts(self):
			# Binding Ctrl+n to newfile funtion
			self.txtarea.bind("<Control-n>",self.newfile)
			# Binding Ctrl+o to openfile funtion
			self.txtarea.bind("<Control-o>",self.openfile)
			# Binding Ctrl+s to savefile funtion
			self.txtarea.bind("<Control-s>",self.savefile)
			# Binding Ctrl+a to saveasfile funtion
			self.txtarea.bind("<Control-a>",self.saveasfile)
			# Binding Ctrl+e to exit funtion
			self.txtarea.bind("<Control-e>",self.exit)
			# Binding Ctrl+x to cut funtion
			self.txtarea.bind("<Control-x>",self.cut)
			# Binding Ctrl+c to copy funtion
			self.txtarea.bind("<Control-c>",self.copy)
			# Binding Ctrl+v to paste funtion
			self.txtarea.bind("<Control-v>",self.paste)
			# Binding Ctrl+u to undo funtion
			self.txtarea.bind("<Control-u>",self.undo)
		# Creating TK Container
	root = Tk()
	# Passing Root to TextEditor Class
	TextEditor(root)
	# Root Window Looping
	root.mainloop()

def devEditorMain():
	class TextEditor:
		# Defining Constructor
		def __init__(self,root):
			# Assigning root
			self.root = root
			# Title of the window
			self.root.title("Bork")
			# Window Geometry
			self.root.geometry("1200x700+200+150")
			# Initializing filename
			self.filename = None
			# Declaring Title variable
			self.title = StringVar()
			# Declaring Status variable
			self.status = StringVar()
			# Creating Titlebar
			self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
			# Packing Titlebar to root window
			self.titlebar.pack(side=TOP,fill=BOTH)
			# Calling Settitle Function
			self.settitle()
			# Creating Statusbar
			self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
			# Packing status bar to root window
			self.statusbar.pack(side=BOTTOM,fill=BOTH)
			# Initializing Status
			self.status.set("Welcome To Bork")
			# Creating Menubar
			self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
			# Configuring menubar on root window
			self.root.config(menu=self.menubar)
			# Creating File Menu
			self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding New file Command
			self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
			# Adding Open file Command
			self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
			# Adding Save File Command
			self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
			# Adding Save As file Command
			self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
			# Adding Seprator
			self.filemenu.add_separator()
			# Adding Exit window Command
			self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
			# Cascading filemenu to menubar
			self.menubar.add_cascade(label="File", menu=self.filemenu)
			# Creating Edit Menu
			self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding Cut text Command
			self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
			# Adding Copy text Command
			self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
			# Adding Paste text command
			self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
			# Adding Seprator
			self.editmenu.add_separator()
			# Adding Undo text Command
			self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
			# Cascading editmenu to menubar
			self.menubar.add_cascade(label="Edit", menu=self.editmenu)
			# Creating Help Menu
			self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
			# Adding About Command
			self.helpmenu.add_command(label="About",command=self.infoabout)
			# Cascading helpmenu to menubar
			self.menubar.add_cascade(label="Help", menu=self.helpmenu)
			# Creating Scrollbar
			scrol_y = Scrollbar(self.root,orient=VERTICAL)
			# Creating Text Area
			self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
			# Packing scrollbar to root window
			scrol_y.pack(side=RIGHT,fill=Y)
			# Adding Scrollbar to text area
			scrol_y.config(command=self.txtarea.yview)
			# Packing Text Area to root window
			self.txtarea.pack(fill=BOTH,expand=1)
			# Calling shortcuts funtion
			self.shortcuts()
			# Defining settitle function
		def settitle(self):
			# Checking if Filename is not None
			if self.filename:
				# Updating Title as filename
				self.title.set(self.filename)
			else:
				# Updating Title as Untitled
				self.title.set("Untitled")
			# Defining New file Function
		def newfile(self,*args):
			# Clearing the Text Area
			self.txtarea.delete("1.0",END)
			# Updating filename as None
			self.filename = None
			# Calling settitle funtion
			self.settitle()
			# updating status
			self.status.set("New File Created")
			# Defining Open File Funtion
		def openfile(self,*args):
			# Exception handling
			try:
				# Asking for file to open
				self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
				# checking if filename not none
				if self.filename:
					# opening file in readmode
					infile = open(self.filename,"r")
					# Clearing text area
					self.txtarea.delete("1.0",END)
					# Inserting data Line by line into text area
				for line in infile:
					self.txtarea.insert(END,line)
				# Closing the file  
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Opened Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
			# Defining Save File Funtion
		def savefile(self,*args):
		# Exception handling
			try:
				# checking if filename not none
				if self.filename:
					# Reading the data from text area
					data = self.txtarea.get("1.0",END)
					# opening File in write mode
					outfile = open(self.filename,"w")
					# Writing Data into file
					outfile.write(data)
					# Closing File
					outfile.close()
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Saved Successfully")
				else:
					self.saveasfile()
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining Save As File Funtion
		def saveasfile(self,*args):
		# Exception handling
			try:
				# Asking for file name and type to save
				untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
				# Reading the data from text area
				data = self.txtarea.get("1.0",END)
				# opening File in write mode
				outfile = open(untitledfile,"w")
				# Writing Data into file
				outfile.write(data)
				# Closing File
				outfile.close()
				# Updating filename as Untitled
				self.filename = untitledfile
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Saved Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining Exit Funtion
		def exit(self,*args):
			op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
			if op>0:
				self.root.destroy()
				devPage()
			else:
				return
		# Defining Cut Funtion
		def cut(self,*args):
			self.txtarea.event_generate("<<Cut>>")
		# Defining Copy Funtion
		def copy(self,*args):
			self.txtarea.event_generate("<<Copy>>")
		# Defining Paste Funtion
		def paste(self,*args):
			self.txtarea.event_generate("<<Paste>>")
		# Defining Undo Funtion
		def undo(self,*args):
		# Exception handling
			try:
				# checking if filename not none
				if self.filename:
					# Clearing Text Area
					self.txtarea.delete("1.0",END)
					# opening File in read mode
					infile = open(self.filename,"r")
					# Inserting data Line by line into text area
					for line in infile:
						self.txtarea.insert(END,line)
					# Closing File
					infile.close()
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Undone Successfully")
				else:
					# Clearing Text Area
					self.txtarea.delete("1.0",END)
					# Updating filename as None
					self.filename = None
					# Calling Set title
					self.settitle()
					# Updating Status
					self.status.set("Undone Successfully")
			except Exception as e:
				messagebox.showerror("Exception",e)
		# Defining About Funtion
		def infoabout(self):
			messagebox.showinfo("About Text Editor","Bork is a simple text editor included inside of Bear-Shell")
		# Defining shortcuts Funtion
		def shortcuts(self):
			# Binding Ctrl+n to newfile funtion
			self.txtarea.bind("<Control-n>",self.newfile)
			# Binding Ctrl+o to openfile funtion
			self.txtarea.bind("<Control-o>",self.openfile)
			# Binding Ctrl+s to savefile funtion
			self.txtarea.bind("<Control-s>",self.savefile)
			# Binding Ctrl+a to saveasfile funtion
			self.txtarea.bind("<Control-a>",self.saveasfile)
			# Binding Ctrl+e to exit funtion
			self.txtarea.bind("<Control-e>",self.exit)
			# Binding Ctrl+x to cut funtion
			self.txtarea.bind("<Control-x>",self.cut)
			# Binding Ctrl+c to copy funtion
			self.txtarea.bind("<Control-c>",self.copy)
			# Binding Ctrl+v to paste funtion
			self.txtarea.bind("<Control-v>",self.paste)
			# Binding Ctrl+u to undo funtion
			self.txtarea.bind("<Control-u>",self.undo)
		# Creating TK Container
	root = Tk()
	# Passing Root to TextEditor Class
	TextEditor(root)
	# Root Window Looping
	root.mainloop()

def backgroundProcess():
	clearScreen()
	print("Bear-Shell Frame Work")
	print("Ver 13021")
	cwd = os.getcwd()
		
	def helpCom():
		clearScreen()
		print("""
		UserInfo: Tells you current user's information
		Root: Allows root terminal access
		python3: Allows you to run .py files
		clear: Clears screen
		ls: shows contents of given directory
		pwd: shows current directory
		restart: restarts the OS
		cd: allows you to access a directory
		cat: allows you to view the contents of a file
		git: allows you to run basic git commands
		(Linux Only!) neofetch: shows system info
		(Linux Only!) apt-get: allows you to run basic apt-get commands like: install, remove, update, and upgrade
		usage: CPU and RAM usage
		exit: quits shell


		More commands to come with future updates:
		""")
	while True:
		f = input("~ $ ")
		if f == "Help":
			clearScreen()
			helpCom()
		elif f == "help":
			clearScreen()
			helpCom()

		elif f == "exit":
			os.system('exit')
			sys.exit()

		elif f == "UserInfo":
			clearScreen()
			b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
			if b_login == l_p:
				print("Username: " + l_n)
				print("Password: " + l_p)
			else:
				print("Wrong password")

		elif f == "userinfo":
			clearScreen()
			b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
			if b_login == l_p:
				print("Username: " + l_n)
				print("Password: " + l_p)
			else:
				print("Wrong password")

		elif f == "root":
			login = input("To access the root terminal, please enter your password: ")
			if login == l_p:
				dec = input(f"{bcolors.FAIL}Are you sure you want to enter the root terminal?{bcolors.HEADER} ")
				if dec == 'y':
					rootTerm()
				elif dec == 'Y':
					rootTerm()
				elif dec == 'n':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
				elif dec == 'N':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()

		elif f == "Root":
			login = input("To access the root terminal, please enter your password: ")

			if login == l_p:
				dec = input("Are you sure you want to enter the root terminal? ")
				if dec == 'y':
					rootTerm()
				elif dec == 'Y':
					rootTerm()
				elif dec == 'n':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
					break
				elif dec == 'N':
					print("Returning to regular terminal...")
					time.sleep(0.5)
					terminalMain()
					break

			elif login != l_p:
				print("Wrong password!")

		elif f == "clear":
			clearScreen()

		elif f == "Clear":
			clearScreen()

		elif f == "python3":
			m = input("What file would you like to run? ")
			if m.endswith('.py'):
				os.system(f'python3 {m}')
			else:
				print(m + " is not a py file.")

		elif f == "ls":
			foo = input("What directory would you like to look through? ")
			isdir = os.path.isdir(foo)

			if isdir:
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + foo)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + foo)

			elif foo == 'ls':
				if name == 'nt':
					print(f"{bcolors.WARNING}")
					_ = system('dir ' + cwd)
				else:
					print(f"{bcolors.WARNING}")
					_ = system('ls ' + cwd)

			else:
				errorHandle("That directory isn't valid!", ErrorCodes.Err6)

		elif f == "pwd":
			print(cwd)

		elif f == "restart":
			print("Restarting...")
			time.sleep(1)
			os.system("python3 BearCMDos.py")

		elif f == "Restart":
			print("Restarting...")
			time.sleep(1)
			os.system("python3 BearCMDos.py")

		elif f == "Pwd":
			print(cwd)

		elif f == "cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

		elif f == "Cd":
			fi = input("Where would you like to go? ")
			workdir = os.path.isdir(fi)
			if workdir:
				perms = os.access(fi, os.R_OK)
				if name == 'nt':
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder!")
				else:
					perms = os.access(fi, os.R_OK)
					if perms:
						system('cd ' + fi)
						cwd = fi
					else:
						print("You don't have permission to access that folder! ")

			else:
				errorHandle("Directory doesn't exist!", ErrorCodes.Err6)

		elif f == "neofetch":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				_ = system('neofetch')

		elif f == "apt-get":
			if name == 'nt':
				print("This command isn't available on your OS!")
			else:
				while True:
					food = input("Would you like to run apt-get update, install, remove, or upgrade? ")
					if food == "update":
						print(f"{bcolors.WARNING}")
						system('sudo apt-get update')
						break

					elif food == "install":
						ding = input("What package do you want to install? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get install ' + ding)
						break
					
					elif food == "remove":
						fing = input("What package would you like to remove? ")
						print(f"{bcolors.WARNING}")
						system('sudo apt-get remove ' + fing)
						break

					elif food == "upgrade":
						bing = input("Are you sure you want to upgrade? ")
						if bing == 'y':
							print(f"{bcolors.WARNING}")
							system('sudo apt-get dist-upgrade')

						else:
							print("Cancelling...")
							time.sleep(1)
							break
					
					else:
						print("Not an option!")

		elif f == 'pip':
			while True:
				daisd = input("What pip package would you like to install? ")
				if daisd == 'exit':
					break
				else:
					os.system('pip3 install ' + daisd)
			
		elif f == 'git':
			while True:
				bing = input("What git command would you like to run? (git init, git add, git commit, git branch, git remote add origin, or git push ('exit' to leave)) ")
				if bing == 'git init':
					system('git init')
				elif bing == 'git add':
					jaf = input("What files would you like to add? (* for all): ")
					system('git add ' + jaf)
				elif bing == 'git commit':
					fjd = input("What would you like the commit message to be? ")
					fling = f'"{fjd}"'
					system('git commit -m ' + fling)
				elif bing == 'git branch':
					sad = input("What branch do you want to use? ")
					system('git branch -M '+ sad)
				elif bing == 'git remote add origin':
					bva = input("What remote origin thing or whatever do you want to add? ")
					system('git remote add origin ' + bva)
				elif bing == 'git push':
					fja = input("What branch do you want to push too? ")
					system('git push -u ' + fja)
				elif bing == 'exit':
					print("Leaving git...")
					time.sleep(1)
					break

				else:
					errorHandle("Not a valid command! ", ErrorCodes.ErrCode1)
					print(f"{bcolors.WARNING}")

		elif f == 'cat':
			faf = input("What file would you like to look into? ")
			if name == 'nt':
				
				_ = system('type ' + faf)
				print("\n")
			
			else:
				print(f"{bcolors.WARNING}")
				_ = system('cat ' + faf)
				print("\n")	

		elif f == 'usage':
			print("Press 'q' to stop")
			while True:

				if keyboard.is_pressed('q'):
					print("Quiting...")
					time.sleep(.43223124)
					clearScreen()
					break
			
				time.sleep(1)
				clearScreen()
				print('CPU: {} %'.format(cpuUsage()))
				print('RAM: {} MB'.format(int(ramUsage() / 1024 / 1024)))
				

		else:
			print("Command does not exist!")	

def testingTerm():
	clearScreen()
	print("Bear-Shell Frame-Work (Portal)")
	print("Ver 13022a")
	print("Type the command 'test' to continue to full terminal")
	while True:
		f = input("~ $ ")
		if f == "test":
			rootTest()
			break
				
		else:
			print("Command does not exist!")	

def rootTest():
	clearScreen()
	print("Bear-Shell Frame Work (Testing) (root)")
	print("Ver 13023a")
	cwd = os.getcwd()
		
	def helpCom():
		clearScreen()
		print("""
		clear:   Clears screen
		ls:      Shows contents of given directory
		pwd:     Shows current directory
		restart: Restarts the OS
		cd:      Allows you to access a directory
		cat:     Allows you to view the contents of a file
		usage:   CPU and RAM usage
		exit:    Quits shell
		vim:     Starts the "Vim" editor

		Flags:
		  -y: only works for the 'restart' command. Usage: 'restart -y'; automatically answers 'y' to prompt
		Update Flags:
		  --full:    Begins a full system update
		  --help:    Shows all valid flags for the 'update' command
		  --version: Checks if the current version of Bear-Shell is up-to-date and applicable for update
		Exit Flags:
		  -admin:    Allows user to exit to the admin menu
		  -user:     Allows user to exit to the regular user menu

		More commands to come with future updates:
		""")
	while True:
		bear = input("~ ( " + str(cwd) + " )" " $ ")
		bear_split = bear.split()
		bear_len = len(bear_split)

		if bear_len == 1:
			com = bear.lower()
			if com == 'restart':
				while True:
					cleets = input("Are you sure you want to restart (y/n)? ")
					if cleets == 'y':
						reset()
						break
					else:
						print("Going back...")
						time.sleep(1)
						testingTerm()
						break

			elif com == 'help':
				try:
					helpCom()
				except ValueError:
					print("Command Failed...")
				else:
					print("Command Executed!")

			elif com == 'pwd':
				print(cwd)

			elif com == 'exit':
				while True:
					ads = input("Would you like to go back to admin page or user page? (type 'admin' or 'user') ")
					adz = ads.lower()
					if adz == 'admin':
						while True:
							log = input("Enter Password To " + "Admin" + " To Login: ")
							if log == '559907':
								print("Opening Dev Page...")
								time.sleep(0.5)
								clearScreen()
								devPage()
								break
					if adz == 'user':
						while True:
							log = input("Enter Password To " + l_n + " To Login: ")
							if log == l_p:
								print("Opening Home Page...")
								time.sleep(0.5)
								clearScreen()
								homePage()
								break
					else:
						print("That is not an option!")

			elif com == 'clear':
				clearScreen()

			elif com == 'ls':
				if name == 'nt':
					_ = system("dir")
				else:
					_ = system("ls")

			elif com == 'vim':
				system('"C:/Program Files (x86)/Vim/vim82/vim.exe"')

			else:
				print("Not a command!")

		elif bear_len > 1:
			bearbear = str(bear_split[0])
			com1 = bearbear.lower()
			if com1 == 'ls':
				direc = str(bear_split[1])
				foofdir = os.path.isdir(direc)
				if foofdir:
					if name == 'nt':
						_ = os.system('dir ' + direc)
					else:
						_ = system('sudo ls '+ direc)
				else:
					print("Not a valid directory")

			elif com1 == 'cd':
				direc = str(bear_split[1])
				foofa = os.path.isdir(direc)
				if foofa:
					if name == 'nt':
						os.system('cd ' + direc)
						cwd = direc
					else:
						os.system('sudo cd ' + direc)
						cwd = direc
				else:
					print("Not a valid directory!")

			elif com1 == 'restart':
				flag = str(bear_split[1])
				if flag == '-y':
					reset()
					break

			elif com1 == 'vim':
				file = str(bear_split[1])
				if name == 'nt':
					_ = system('"C:/Program Files (x86)/Vim/vim82/vim.exe" ' + file)
				else:
					_ = system('vim ' + file)

			elif com1 == 'exit':
				flag2 = str(bear_split[1])
				if flag2 == '-admin':
					while True:
						log = input("Enter Password To " + "Admin" + " To Login: ")
						if log == '559907':
							print("Opening Dev Page...")
							time.sleep(0.5)
							clearScreen()
							devPage()
							break
						else:
							print("Incorrect!")
				elif flag2 == '-user':
					print("Returning to menu...")
					time.sleep(0.5)
					clearScreen()
					homePage()

			elif com1 == 'update':
				flag3 = str(bear_split[1])
				if flag3 == '--full':
					print("Checking for updates...")
					print("This may take a while!")
					time.sleep(1)
					from dotenv import load_dotenv
					from github import Github
					clearScreen()
					load_dotenv()
					token = os.environ.get("api")
					g = Github(token)
					repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
					print("Checking for updates...")
					v = repo.get_contents("ver.txt")
					f = v.decoded_content
					print("Current Github Repo Version: " + str(f))
					print("Checking if up-to-date...")
					time.sleep(1)
					if str(f) == "b'1.3.3'":
						clearScreen()
						print("You're up to date!")
						print("The system wont be updated.")
						time.sleep(1)
						clearScreen()
						rootTest()
					else:
						while True:
							d = input("You aren't up-to-date. Update? ")
							if d == 'n':
								print("Returning to terminal...")
								time.sleep(1)
								rootTest()
								break
							elif d == 'y':
								pass
							else:
								print("That isn't a command!")
				elif flag3 == '--help':
					print("Valid update flags: ")
					print("--help:    Shows all valid flags for the 'update' command")
					print("--full:    Begins full update")
					print("--version: Checks if there is an update available")

				elif flag3 == '--version':
					from dotenv import load_dotenv
					from github import Github
					clearScreen()
					load_dotenv()
					token = os.environ.get("api")
					g = Github(token)
					repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
					print("Checking version...")
					v = repo.get_contents("ver.txt")
					f = v.decoded_content
					print("Current Github Repo Version: " + str(f))
					print("Checking if up-to-date...")
					time.sleep(1)
					if str(f) == "b'1.3.3'":
						clearScreen()
						print("You're up to date!")
						print("No need for an update")
						time.sleep(1)
						clearScreen()
						rootTest()
					else:
						print("Your Bear-Shell is out of date! Run the command: 'update --full' to update the system")

				else:
					print("Command error encountered: No flag supplied")
					print("Run the command: 'update --help' for info on update command flags")
				
			elif com1 == 'cat':
				from os.path import exists
				flag4 = str(bear_split[1])
				c = exists(flag4)
				if c:
					if name == 'nt':
						_ = system("type " + flag4)
						print("")
					else:
						_ = system("cat " + flag4)
						print("")
				else:
					print("File doesn't exist!")

			elif bear_len > 2:
				bearv1 = str(bear_split[0])
				bearv2 = str(bear_split[1])
				bearv3 = str(bear_split[2])
				print(bearv1)
				print(bearv2)
				print(bearv3)

			else:
				print("Not a command!")

def calculator():
	clearScreen()
	print("Type the 'e' command to exit")
	while True:
		print("""
		[+] For addition
		[-] For subtraction
		[*] For multiplication
		[/] For division
		""")
		ddd = input("Command: ")

		if ddd == '+':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.add(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						homePage()
						break
		elif ddd == '-':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.sub(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						homePage()
						break
						

		elif ddd == '*':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.multiply(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						homePage()
						break

		elif ddd == '/':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.divide(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						homePage()
						break
		elif ddd == 'e':
			print("Going back to main menu...")
			time.sleep(1)
			clearScreen()
			homePage()
			break
		else:
			print("That command wasn't found!")

def devCalculator():
	clearScreen()
	print("Type the 'e' command to exit")
	while True:
		print("""
		[+] For addition
		[-] For subtraction
		[*] For multiplication
		[/] For division
		""")
		ddd = input("Command: ")

		if ddd == '+':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.add(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						devPage()
						break
		elif ddd == '-':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.sub(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						devPage()
						break
						

		elif ddd == '*':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.multiply(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						devPage()
						break

		elif ddd == '/':
			clearScreen()
			while True:
				addition = input("Enter 2 nums: ")
				add_split = addition.split()
				if len(add_split) > 1:
					add1 = add_split[0]
					add2 = add_split[1]
					print(cb.divide(add1, add2))
				else:
					first = add_split[0]
					if first == 'e':
						print("Going back to menu...")
						time.sleep(1)
						clearScreen()
						devPage()
						break
		elif ddd == 'e':
			print("Going back to main menu...")
			time.sleep(1)
			clearScreen()
			devPage()
			break
		else:
			print("That command wasn't found!")

def sysInfo():
	import os
	testing = open('gitbranch.txt')
	test = testing.read()
	varss = open('data/version.data')
	var = varss.read()
	from dotenv import load_dotenv
	from github import Github
	clearScreen()
	load_dotenv()
	token = os.environ.get("api")
	g = Github(token)
	repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
	v = repo.get_contents("ver.txt")
	f = v.decoded_content
	if str(f) == "b'1.3.3'":
		upDate = "Up-To-Date!"
	else:
		upDate = "Out-Of-Date!"

	if name == 'nt':
		os = "Windows"
	else:
		os = "Linux"

	if test == 'true':
		gitBranch = "True "
	else:
		gitBranch = "False"

	while True:
		print(f"""
Current Shell: Version {var}
Current OS: {os}
Up-To-Date: {upDate}
Python Version: {version}
Using Testing Branch: {gitBranch}
----------------------------
Bear-Shell; Created by Michael S.
		""")
		a = input("com: ")
		b = a.lower()
		if b == 'e':
			print("Exiting...")
			clearScreen()
			homePage()
			break

def devSysInfo():
	import os
	testing = open('gitbranch.txt')
	test = testing.read()
	varss = open('data/version.data')
	var = varss.read()
	from dotenv import load_dotenv
	from github import Github
	clearScreen()
	load_dotenv()
	token = os.environ.get("api")
	g = Github(token)
	repo = g.get_repo("BizzyPythonBear/Bear-Shell-Unstable")
	v = repo.get_contents("ver.txt")
	f = v.decoded_content
	if str(f) == "b'1.3.3'":
		upDate = "Up-To-Date!"
	else:
		upDate = "Out-Of-Date!"

	if name == 'nt':
		os = "Windows"
	else:
		os = "Linux"

	if test == 'true':
		gitBranch = "True "
	else:
		gitBranch = "False"

	while True:
		print(f"""
Current Shell: Version {var}
Current OS: {os}
Up-To-Date: {upDate}
Python Version: {version}
Using Testing Branch: {gitBranch}
----------------------------
Bear-Shell; Created by Michael S.
		""")
		a = input("com: ")
		b = a.lower()
		if b == 'e':
			print("Exiting...")
			clearScreen()
			devPage()
			break

# | Ignore |
#
# ['2', '6']
#  2 = 0 <- When counting items, it starts at 0, not 1.
#  6 = 1

# When this file is ran, clear the screen
clearScreen()
writeVersionNum(bear_shell)
makeTest()
#  To-Do
# --------------------
# [X] Finish Calculator
# [ ] Add A web-browser