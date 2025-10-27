# receive_sms_example.py [v20250930]

"""
Example: receive SMS messages and print them to the REPL.
Each sushi.cmd(...) call returns a tuple:
    [0] = function result (0 = no error)
    [1] = result or error message if err ≠ 0
"""

print("SMS receiving example...\n")

# --- Callback executed on modem events ---
# a[0] = event type (0=SMS received, 1=Incoming call, 2=SMS TX result)
# a[1..] = event-specific data
def modem_callback(a):
    if a[0] == 0:  # SMS received
        number = a[1]
        text   = a[2]
        time   = a[3]
        print("SMS received:")
        print("  From :", number)
        print("  Text :", text)
        print("  Time :", time)
    else:
        # ignore other events for this example
        pass

# --- Register callback ---
sushi.cmd("set_modem_hnd", modem_callback)
print("Modem callback registered. Incoming SMS will be displayed here.")