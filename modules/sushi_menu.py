# sushi_menu.py
this_file_version="2025-11-05@1911"

"""sushi_menu.py
    Classes for user menu management with Sushi Framework"""
import sushi as sb

class Submenu:
    """Submenu class"""
    def __init__(self, title):
        """
        Create a new sub-menu entry
        Args:
            title (str): menu title
        """
        self.title = title
        r = sb.cmd('new_menu' , title)
        if r[0] == 0: # no errors 
            self.id = r[1]		#menu handle ID
            sb.cmd('add_entry_to_menu' , (0,self.id)) #add submenu to home menu (ID 0)
    def add_enum_editable_item(self , name , onchange , value_index , *values):
        """
        Add an entry of editable list of values
        Args:
            name (str) : entry name shown in the menu
            onchange (func) : callback function called when the value changes
            value_index (int) : initial value index (0,1,2,...)
            *values (str...): list of values (example "OFF","ON")
        Returns:
            id (int) : new menu entry ID
        """
        r = sb.cmd('new_menu_item_edit_list' , (name , onchange , value_index) + values )
        if r[0] == 0:# menu successfully added
            sb.cmd('add_entry_to_menu' , (self.id,r[1]))	# adding new menu item to this menu
            return r[1]
        # for i, p in enumerate(values, 1):
        #    print(f"Parametro {i}: {p}")
    def add_read_only_item(self , name , onprint):
        """
        Add a read-only entry 
        Args:
            name (str) : entry name shown in the menu
            onprint (func) : callback function to be called to print the value
        Returns:
            id (int) : new menu entry ID
        """
        r = sb.cmd('new_menu_item_string' , (name , onprint) ) # create new menu item
        if r[0] == 0: # menu successfully added
            sb.cmd('add_entry_to_menu' , (self.id,r[1]))	# adding new menu item to this menu 
            return r[1]
def help():
    # Version
    print(f"Module 'sushi_menu.py'")
    print()
    print(f"* Description: User menu management")
    print(f"* Version:'{this_file_version}'")
    print(f"* Functions: call `sushi.help()`")
    

"""
**Submenu class in `sushi_menu` module**
    
* `Submenu(menu_title:str)`  
  Create a new "Submenu" item
* Submenu methods:  
  - `add_enum_editable_item(name, onchange , value_index , *values)`  
    Add an entry with a selectable list of values  
    Args:  
      . name (str)        : entry name shown in the menu  
      . onchange (func)   : callback called when value changes  
      . value_index (int) : initial value index (0,1,2,...)  
      . *values (str...)  : list of values (e.g. "OFF","ON")  
    Returns:  
      id (int) : new menu entry ID  
  - `add_read_only_item(name, onprint)`  
    Add a read-only entry  
    Args:  
      . name (str)       : entry name shown in the menu  
      . onprint (func)   : callback called to print the value  
    Returns:  
      id (int) : new menu entry ID  
* Example: see [menu_example.py](https://github.com/sushi-iot/sushi-iot-framework/tree/main/examples)  
"""
    
    
"""
# CORE CALLS
! These are lower level calls used in this module.

* `sushi.cmd("new_menu", title:str)` -> int (menu_id)
  Create a new menu with the given title
* `sushi.cmd("new_menu_item_string", (desc:str, print_cb:func))` -> int (entry_id)
  Create a new string menu item with a callback for printing
* `sushi.cmd("new_menu_item_edit_list", (desc:str, changed_cb:func, init_index:int, val1:str, val2:str, ...))` -> int (entry_id)
  Create a new editable list menu item with initial value and change callback
* `sushi.cmd("add_entry_to_menu", (menu_id:int, entry_id:int))` 
  Add an entry to the specified menu
"""
