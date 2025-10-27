# Sushi IoT Framework microPython quick reference  

## sushi.help()
```python
>>> sushi.help()
*This_help_version: 2025-10-22*  
*Compatibility: sushi-iot_v25.08.29.0*  

## GENERAL INFO ##

**CORE MODULE**  

* `sushi` is the core module.  
* All calls to the core module `sushi.cmd("command",...)` return a tuple: (`err`:int, `result`:var)  
  - if `err` = 0   => OK, `result` contains the command-specific value  
  - if `err` != 0  => ERROR, `result` contains the error message (str)  

**FROZEN MODULES**  

* Integrated "frozen" `.py` modules are:
  - `sushi_menu` : User menu management  
  - `sushi_utils` : System setup, status & utilities  


**ONLINE DOC**

* [Sushi-IoT documentation]("https://sushi-iot.github.io/sushi-iot-framework/")
* [GitHub-Home]("https://github.com/sushi-iot/sushi-iot-framework")
* [GitHub-Examples]("https://github.com/sushi-iot/sushi-iot-framework/tree/main/examples")

---
## SYSTEM ##
* `sushi.cmd("help")` -> str   
  Show this help
* `sushi.cmd("ver")` -> str  
  Show the firmware version
* `sushi.cmd("restart" [, delay_ms:int=2000])`  
  Restart the board after the optional delay in milliseconds
* `sushi.cmd("set_log", level:int [0=disable,1=enable,255=extended])`  
  Enable or disable REPL logging
* `sushi.cmd("factory_reset")`  
  Restore factory default settings
* `sushi.cmd("log", (type:str ['E'=error,'S'=status,'D'=debug,'X'=event] , entry:str))`  
  Add an entry to LOG
* `sushi.cmd("register", code:str)`  
  Register the device with a unique 64-character code

---  
## SETUP & STATUS ##
* `sushi_utils.get_sushi_config()` -> dict or None (if error)  
  Return full configuration structure
* `sushi_utils.set_sushi_config(settings:dict )` -> int [0 = value not changed ; 1 = value changed no restart ; 2 = value changed need restart; < 0 = error]  
  Set configuration parameters (self restart if settings changed).
* `sushi_utils.list_params(module:str ['system' , 'wifi'])`  
  List the available configuration params
* `sushi_utils.get_sushi_status()` -> dict or None (if error)  
  Return full status structure
* `sushi_utils.load_setting(module:str, setting_str)`  -> str or int or None (if error)  
  Load a custom configuration parameter
* `sushi_utils.save_setting(module:str, setting:str, value:int or str)`  -> int [0 = value not changed ; 1 = value changed ; < 0 = error]  
  Save a custom configuration parameter  

---
## WIFI COMMANDS ##
* `sushi.cmd("wifi_stop")`  
  Stop wifi management
* `sushi.cmd("wifi_restart")`  
  Restart wifi management
* Configuration: see "SETUP & STATUS" section.  

---
## MODEM ##
* `sushi.cmd("set_modem_hnd", callback:func)`  
  Set a callback to handle modem events.  
  `callback` args: (a:tuple)  
    - a[0] = event type [0=SMS received, 1=Incoming call, 2=SMS TX result]  
    - a[1..] = event-specific data:  
      . if a[0] = 0 → (call_number:str, sms_text:str, time:str)  
      . if a[0] = 1 → (call_number:str)  
      . if a[0] = 2 → (id:int, tx_result:int [1=OK, 0=ERROR])  
* `sushi.cmd("send_sms", (text:str, number:str))` -> int  
  Send an SMS message; returns the SMS ID if command accepted

---
## POWER ##
* `sushi.cmd("read_power_state")` -> int [1=ON, 0=OFF]  
  Get the main power state
* `sushi.cmd("read_power_voltage")` -> float (V)  
  Read the main power voltage
* `sushi.cmd("read_batt_level")` -> float (perc)  
  Get the battery level in percent
* `sushi.cmd("read_batt_voltage")` -> float (V)  
  Read the battery voltage
 
---
## MENU ##

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
	  
---
## GPIO & SENSORS ##
* `sushi_utils.pinout()` -> str  
  Return the board pinout for integrated & general purpose functions
* `sushi.cmd("read_temperature", sensor:int [0=DS18B20-1,1=DS18B20-2])` -> float (°C)  
  Read temperature from the selected sensor
* `sushi.cmd("read_ext_gpin", source:int [0=IO-Expander])` -> int (status)  
  Read external digital input from the specified source
* `sushi.cmd("set_ext_gpin_int", callback:func)`  
  Set a callback to detect changes in external input state
  `callback` args :(source:int [0 = IO-Expander])
* `sushi.cmd("set_out_state", (name:str ["RELAY_1..N" , "BUZZER" , "GPIO_1..N" , ... ] , state:int [0 ,1]))`  
  Set digital out state by name
* `sushi.cmd("add_out", (name:str  , pin:int))`  
  Set a pin as out and link to a name

```

## sushi_utils.help()

```python
>>> sushi_utils.help()
Module 'sushi_utils.py'

* Version:'2025-10-22@2047'
* Compatibility:'sushi-iot_v25.08.29.0+'
* Functions: call `sushi.help()`
* Examples: call `sushi_utils.help('examples')`
```

## sushi_utils.pinout()

```python
>>> sushi_utils.pinout()
Available boards:

*  ID 0: ESP32-DevKitC on Sushi Board

Use pinout(<ID>) to view details.
```

### sushi_utils.pinout(0) [ESP32-DevKitC on Sushi Board]

```python
>>> sushi_utils.pinout(0)
=== ESP32-DevKitC on Sushi Board ["board_model" ID: 0] ===


* ONLINE DOC
    -> ESP32-DevKitC: "https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html"
    -> Sushi Board: "https://sushi-iot.github.io/sushi-iot-board/"

### PINOUT

#system(always present)
* ON-BOARD-BUTTON: 0
* I2C_SDA_PIN:21
* I2C_SCL_PIN:22
* REPL_UART1_TX:19
* REPL_UART1_RX:18
* VIN-ADC:36(VP)

#GPIO(free I/O pins) 
* GPIO_1:19
* GPIO_2:18
* GPIO_3:5
* GPIO_4:4
* GPIO_5:13
#GPI(free Input only pins)
* GPI_1:39(VN)
* GPI_2:35
#GPO(free Output only pins)
* GPO_1:2

#power(if 'battery_enable' > 0)
* BATT-ADC:34

#modem(if 'modem_enable' > 0)
* MODEM_UART_TX:27
* MODEM_UART_RX:26	
* MODEM_PWKEY:32
* MODEM_POWER:23

#io-expander(if 'ioex_enable' > 0)
* IOEXP_I2C_INT_PIN:14

#direct 4B keyboard(if 'keyboard_enable'=100)
* COMMON: GND
* IN_1: GPIO_2
* IN_2: GPIO_3
* IN_3: GPIO_4
* IN_4: GPIO_5

#relays
* RELE_1_PIN:15 (if 'rele_out_enable'>0)
* RELE_2_PIN:12 (if 'rele_out_enable'=2)

#temperature sensor(if 'ext_temperature_sensor_enable' > 0)
* DS18B20_DATA:33

#buzzer(if 'buzzer_enable' > 0)
* BUZZER_PIN:25
```

## sushi_utils.list_params()

```python
>>> sushi_utils.list_params()
No help available for module 'None'

Available modules:
  * 'system'
  * 'wifi'

Call list_params('MODULE') to see parameters of a module
```

### sushi_utils.list_params('system')

```python
>>> sushi_utils.list_params('system')
### Parameters for module 'system':

## SYSTEM-CONFIG params
* device_name (str): Device name/description
  Values: String
* data_file_version (str): Configuration file version
  Values: String

## SYSTEM-DATETIME params
* time_zone_hours (int): Time zone offset from UTC
  Values: -12…+14
* time_auto_daylight_save_change (int): Enable automatic daylight saving change (European rules)
  Values: 0=disabled;1=enabled
* ntp_server_address (str): NTP server address
  Values: String. Example: 'pool.ntp.org'

## HARDWARE-SETUP params
* board_model (int): Board model. Call 'sushi_utils.pinout()' to see the pinout.
  Values: 0=ESP32-DevKitC on Sushi Board
* ioex_enable (int): Enable I/O expander management
  Values: 0=none;1=PCF8575
* ext_temperature_sensor_enable (int): Enable temperature sensor
  Values: 0=none;1=DS18B20
* rele_out_enable (int): Enable relay outputs
  Values: 0=none;1..2=number of relays
* keyboard_enable (int): Enable keypad management
  Values: 0=none;1...N=N keys on I/O-Expander;100=4 keys on GPIN
* lcd_enable (int): Enable display
  Values: 0=none;1=OLED_SSD1306
* buzzer_enable (int): Enable buzzer
  Values: 0=none;1=buzzer enabled
* battery_enable (int): Battery level range
  Values: 0=none;1=reserved;2=1 li-ion cell (1S) ~3.0–4.2V;3=3 li-ion cells (3S) ~9–12.6V

## SYSTEM-HEALTH&MONITOR params
* event_register_size_kb (int): Event register file size
  Values: 0=no event file;N=Max KB
* system_info_log_frequency_min (int): System info log frequency (minutes)
  Values: 0=never;N=minutes
* system_info_store_frequency_min (int): System info storage frequency (minutes). Requires system_info_csv_filter.
  Values: 0=never;N=minutes
* system_info_csv_filter (str): Filter for system status entries stored when system_info_store_frequency_min ≠ 0
  Values: String: '<entry_info_1>*<entry_info_2>*...'
* system_info_send_http_post_frequency_min (int): HTTP POST system info frequency (minutes). Posts are sent to http_post_delivery_address.
  Values: 0=never;N=minutes

## SYSTEM-INTERFACE params
* wifi_status_led (str): Assign wi-fi status to an external LED
  Values: String: 'GPIO_1..N', 'GPO_1..N' - see HW pinout
* system_status_led (str): Assign system status to an external LED
  Values: String: 'GPIO_1..N', 'GPO_1..N' - see HW pinout
* modem_status_led (str): Assign modem status to an external LED
  Values: String: 'GPIO_1..N', 'GPO1..N' - see HW pinout

## HTTP-DATA-MANAGER params
* http_post_delivery_address (str): Server address for HTTP POST. Custom application-specific data can be sent by the Sushi-IoT-Framework API
  Values: String. Example: 'https://your_web_server/post_data.php'
* use_wifi_for_http_post (int): Use wi-fi before modem for HTTP POST
  Values: 0=disabled;1=enabled

## MODEM params
* modem_enable (int): Enable modem management
  Values: 0=none;1=SIMCOM7672X
* modem_sim_sms_center (str): SIM SMS center number
  Values: String. Example: '+393519999600'
* modem_sim_pin (str): SIM PIN code
  Values: String. Example: '1234'
* modem_apn (str): SIM APN name
  Values: String. Example: 'iliad'
* modem_user (str): APN user
  Values: String. Optional
* modem_passwd (str): APN password
  Values: String. Optional

## DEBUG-EXPERIMENTAL-RESERVED params
* powersave_time_wifi_off_min (int): Auto wi-fi power-off after inactivity (minutes)
  Values: 0=disabled;N=minutes
* debug_mode (int): Debug
  Values: Reserved
* extension_modules (str): Enable extra experimental modules
  Values: Reserved
```

### sushi_utils.list_params('wifi')

```python
>>> sushi_utils.list_params('wifi')
### Parameters for module 'wifi':

## COMMON params
* wifi_mode (int): Wifi mode
  Values: 0=Disabled;1=Client;2=Access point
* ip (str): IP address
  Values: IP address string
* subnet (str): Subnet mask
  Values: IP address string
* gateway (str): Gateway
  Values: IP address string

## WIFI-CLIENT-MODE params
* cli_ssid (str): Network SSID
  Values: String
* cli_passwd (str): Network password
  Values: String
* cli_dhcp_enable (int): Enable DHCP client
  Values: 0=disabled;1=enabled
* cli_dns_address (str): 
  Values: IP address string

## WIFI-ACCESS-POINT-MODE params
* ap_passwd (str): Access point password
  Values: String
* ap_channel (int): Access point channel
  Values: String

```


