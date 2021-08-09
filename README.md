<img src="/imgs/logo.png" width="200" height="200" alt="Bear-Shell logo">

<br>

## What IS Bear-Shell?
Bear-Shell is a command-line based shell developed by [Michael](https://github.com/BizzyPythonBear). This shell specializes in high efficiency and ease of use.

## Quick Find
* [Why You Should Use Bear-Shell](#why)
* [How to Run Bear-Shell](#installation)
* [Compatibility](#comp)
* [Prerequisites](#required)
* [Upcoming Additions/Ideas](#upcome)
* [Newest Updates](#new-update)
* [Old Updates](#old)
* [Current Terminal Commands](#current)
* [Additional Resources/Credits](#add)
* [Developer's Guide](#dev-guide)
* [Framework](#framework)
* [Extra Things](#extras)

<a name="why"></a>

## Why should I use Bear-Shell?
I do not expect Bear-Shell to be used for real life applications, as it requires python 3 to be ran. In the future, I will more than likely be adding things like running commands as root, cd'ing into directories, and lots more. As of right now, it basically has the bare minimum to be used as, technically an os. With the new addition of the ls, and pwd command, you can now navigate even inside of the terminal.

<a name="installation"></a>

## Running and installing
To run/install the shell, run the command: ```make start```
To uninstall the shell, run the command: ```make uninstall```

<a name="comp"></a>

## Compatibility
As of now, Bear-Shell is compatible with Windows and Linux. No plans have been made to make Macintosh compatibility.


<a name="required"></a>

## Prerequisites
To use Bear-Shell, you'll need to install:
- Python 3.*
- Tkinter (pip3 install tk)
- Curses (Go to [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses) to install it.)
-	[This](https://stackoverflow.com/questions/32417379/what-is-needed-for-curses-in-python-3-4-on-windows7) goes into more depth on how to install it.
- 	If you are on linux, curses is included with python and wont need to be installed.
- [Vim 8.2](https://www.vim.org/download.php)

<a name="upcome"></a>

## Upcoming Ideas
I have many plans for this Shell. Right now, the biggest thing is the cd command, as it will allow you to stay inside of the Shell without having to leave to navigate to other folders.

Some other ideas:
- ~~Sudo~~
- Cosmetics
- Flavors?

By cosmetics I mean when typing a number in the menu for example, if the number is the same as one of the numbers on the screen, it will be green, but if it is one of the numbers that aren't listed in the menu, it will show as red.

By flavors I mean making new flavors of Bear-Shell, like Ubuntu is a flavor of Debian, and such.

<a name="new-update"></a>

## Newest Updates
<b>Disclaimer!</b> Patches will not be shown here! This area is for big releases only! The third digit is for patches, and those are pretty much always bug fixes, so they wont be put here.
<br>
In the most recent update, version 2.3.5, is the full migration from the testing branch, to the main branch. (This is because there is only one repository now)

- Migration: Everything that once said (testing), anything that checks if there is a testing branch, essentially everything that has to do with the testing branch has been removed.
- Small Bug fixes

I wanted to add this feature because I thought about Bear-Shell's whole point, which is to be fast, efficient, and easy. Which before this update, you had to manually install some of the libraries/packages. Which isn't very easy, and efficient, so I made it so that all the user has to do is start the shell. (e.g. via ```make```)

<a name="old"></a>

## Older Updates
- Ver 1.3.3   (Patch)
- Ver 1.3.2.2 (Patch)
- Ver 1.3.2.1
- Ver 1.3.1.1
- Ver 1.3.0.1
- Ver 1.3.0
- Ver 1.2.9
- 	 |
- Ver 1.2.1
- Ver 0.2.1
- Ver 0.0.1

To see previous updates, you can go [here](https://github.com/BizzyPythonBear/Bear-Shell/blob/main/prev.txt), or you can run the shell and when in the menu, and go to the update log. (Hit 7 and then Enter)

<a name="current"></a>

## Current Commands 
The current commands that can be used in the included terminal are as listed:
- root
- python3
- ls (When the prompt asks for the directory you want to look through, you can type 'ls' to view the contents of the current directory)
- pwd
- clear
- exit
- userinfo
- cd
- neofetch
- apt-get
- cat
- git

<a name="add"></a>

## Additional Resources Used:
(Text Editor, and Soon, Web Browser)
Bear-Utils: Created by [Michael](https://github.com/BizzyPythonBear)

Everything else has been created by me, terminal, menu, etc.

<a name="dev-guide"></a>

## Guide for Developers
If you're a dev looking to play around with this the developer mode passwords are:
- 559907: Opens up to dev menu
- 559908: Goes right to dev console

<a name="framework"></a>

## Framework Info
If you'd like to view to documentation for the framework included with Bear-Shell read the docs [here.](https://github.com/BizzyPythonBear/Bear-Shell/blob/main/docs/Framework-Docs.md)

<a name="extras"></a>

## Extras
Disclaimer: Updates come out randomly and aren't scheduled.

Updates will also be a little slow, as I suck at organizing my code, so it takes a while for me to find code, update and change things, but I will definitely still be pushing updates out as fast as possible.

If you'd like to contact me, shoot me a DM on discord at ```MicBearr#5816```