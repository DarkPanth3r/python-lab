# pre-requisite:
# Install library pynput with the command:
#   pip install pynput
# Further info on the Library: https://pypi.org/project/pynput/

#####################################################################
# This script capture all the keys sent to the keyboard
#####################################################################

import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} pressed".format(key)) 

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
