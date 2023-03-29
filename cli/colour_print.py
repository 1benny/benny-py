"""
Coloures, it's spelled the right way
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coloures provides minimum text colour changing operations for Python programs that use Windows cmd.
Usage:

    >>> import coloures
    >>> coloures.colour(text="Hello, World", colour="green")
    Hello, World

"""

from colorama import just_fix_windows_console

just_fix_windows_console()

def printc(text, colour):
    if colour == "red":
        new_text = ('\x1b[1;31;40m' + f'{text}' + '\x1b[0m')
    if colour == "blue":
        new_text = ('\x1b[1;36;40m' + f'{text}' + '\x1b[0m')
    if colour == "green":
        new_text = ('\x1b[1;32;40m' + f'{text}' + '\x1b[0m')
    if colour == "yellow":
        new_text = ('\x1b[1;33;40m' + f'{text}' + '\x1b[0m')
    if colour == "purple":
        ('\x1b[1;35;40m' + f'{text}' + '\x1b[0m')
    
    return new_text