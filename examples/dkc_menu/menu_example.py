# menu_example.py [v202511062242]

"""
Example: Add a custom menu to user interface to switch ON/OFF a relay OUTPUT
Remark: to avoid multiple instances of the same menu, 
        always run this script doing a device "reset and restart"
"""
import sushi
import menu_example_config  # set the configuration for the ESP32DevKitC
from sushi_menu import Submenu
import time

##########################################
# Create new submenu added to home menu
##########################################
mymenu = Submenu('Test Menu')

##########################################
# Add read only menu entry to read a value
##########################################

# Callback called when the menu is print
def menu_print_callback(node): 
    if node == mymenu_entry_sec: #optional check in case that the callback is shared
        return str(time.localtime()[5])	# print the time seconds

# Create a new menu entry
mymenu_entry_sec = mymenu.add_read_only_item("Seconds" , menu_print_callback)

##########################################
# Add a menu entry to set a switch
##########################################

# define the pin to control the relay
from machine import Pin
relay = Pin(15, Pin.OUT) # Sushi board relay 1 out
relay.value(0)  # Init relay OFF

# Callback called when the value change
def menu_onchange_callback(node , value):
    print('changed !')
    if node == mymenu_entry_switch:
          print(f'value:{value}')
          relay.value(value)

# Create a new menu entry
mymenu_entry_switch = mymenu.add_enum_editable_item("Switch" , menu_onchange_callback , 0 , "OFF" , "ON")

