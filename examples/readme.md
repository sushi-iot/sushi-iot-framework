# Sushi IoT Framework microPython examples

## Basic examples

### Bare ESP32DevKitC (Espressif official dev board)  
<img src="../hardware/ESP32DevKitC-WROVER.png" width=10% >

* **[Espressif ESP32DevKitC board](https://github.com/sushi-iot/sushi-iot-framework/tree/main/hardware/ESP32DevKitC-WROVER.md)**

|Name|Description|
|--------|--------|
[dkc_menu](dkc_menu)|Add a custom menu (by 'sushi_menu' module) to user interface to switch ON/OFF a relay OUTPUT

### Sushi Board  
<img src="../hardware/sushi_board_1.png" width=10% >

* **[Sushi Board DOC](https://sushi-iot.github.io/sushi-iot-board/)**  

|Name|Description|
|--------|--------|
[sb_ext_gpin](sb_ext_gpin)|Read IO-Expander input and detect changes via interrupt callback
[sb_read_sensors](sb_read_sensors)|Reads the board’s main sensors (voltage, battery, temperature) and prints the values to the REPL.
[sb_send_sms](sb_send_sms)|Sends an SMS via the modem and shows the result using a callback
[sb_receive_sms](sb_receive_sms)|receive SMS messages and print them to the REPL
[sb_menu](sb_menu)|Add a custom menu (by 'sushi_menu' module) to user interface to switch ON/OFF a relay OUTPUT

## Quick reference
In the REPL, run:
```python
  sushi.help()
```
or see the result directly [here](https://github.com/sushi-iot/sushi-iot-framework/tree/main/examples/sushi-quick-reference.md).

## Resources
[Firmware download](https://github.com/sushi-iot/sushi-iot-framework/releases)    
[Online manual](https://sushi-iot.github.io/sushi-iot-framework/coding/)    
[Sushi IoT project overview](https://sushi-iot.github.io/sushi-iot-framework/)  
