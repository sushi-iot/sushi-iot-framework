# read_sensors_example.py [v20250929]

"""
Example: Reads the board’s main sensors (voltage, battery, temperature) and prints the values to the REPL..
Each sushi.cmd(...) call returns a tuple:
    [0] = function result (0 = no error)
    [1] = sensor value (if no error) or error description (if error)
"""

print("Reading sensors...\n")


# --- Read main power state ---
# 1 = ON, 0 = OFF
res = sushi.cmd("read_power_state")
if res[0] == 0:
    print("Main power state:", "ON" if res[1] == 1 else "OFF")
else:
    print("Error reading power state:", res[0], "(", res[1], ")")


# --- Read main power voltage ---
res = sushi.cmd("read_power_voltage")
if res[0] == 0:
    print("Main power voltage:", res[1], "V")
else:
    print("Error reading power voltage:", res[0], "(", res[1], ")")


# --- Read battery level (percentage) ---
res = sushi.cmd("read_batt_level")
if res[0] == 0:
    print("Battery level:", res[1], "%")
else:
    print("Error reading battery level:", res[0], "(", res[1], ")")


# --- Read battery voltage ---
res = sushi.cmd("read_batt_voltage")
if res[0] == 0:
    print("Battery voltage:", res[1], "V")
else:
    print("Error reading battery voltage:", res[0], "(", res[1], ")")


# --- Read temperature from onboard DS18B20 sensor ---
res = sushi.cmd("read_temperature", 0)
if res[0] == 0:
    print(f"Onboard temperature sensor:", res[1], "°C")
else:
    print(f"Error reading onboard temperature sensor:", res[0], "(", res[1], ")")