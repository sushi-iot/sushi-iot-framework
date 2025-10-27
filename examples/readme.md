# Sushi IoT Framework microPython examples

## Basic examples  
|Name|Description|Supported hardware|
|--------|--------|--------|
[gpin](gpin)|Read IO-Expander input and detect changes via interrupt callback| [Sushi Board](https://sushi-iot.github.io/sushi-iot-board/)
[read_sensors](read_sensors)|Reads the board’s main sensors (voltage, battery, temperature) and prints the values to the REPL.|[Sushi Board](https://sushi-iot.github.io/sushi-iot-board/)
[send_sms](send_sms)|Sends an SMS via the modem and shows the result using a callback|[Sushi Board](https://sushi-iot.github.io/sushi-iot-board/)
[receive_sms](receive_sms)|receive SMS messages and print them to the REPL|[Sushi Board](https://sushi-iot.github.io/sushi-iot-board/)
[menu_example](menu_example)|Add a custom menu (by 'sushi_menu' module) to user interface to switch ON/OFF a relay OUTPUT|* [Sushi Board](https://sushi-iot.github.io/sushi-iot-board/)<br>* Bare [Espressif ESP32DevKitC board](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html)


## Quick reference
In the REPL, run:
```python
  sushi.help()
```
or see the result directly [here](sushi-quick-reference.md).

## Resources
[Firmware download](https://github.com/sushi-iot/sushi-iot-framework/tree/main/firmware)    
[Online manual](https://sushi-iot.github.io/sushi-iot-framework/coding/)    
