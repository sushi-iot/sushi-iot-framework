# send_sms_example.py [v20250930]

"""
Example: Sends an SMS via the modem and shows the result using a callback. 
Each sushi.cmd(...) call returns a tuple:
    [0] = function result (0 = no error)
    [1] = command-specific result or error message if err ≠ 0
"""

print("SMS sending example...\n")

# --- Callback executed on modem events ---
# a[0] = event type (0=SMS received, 1=Incoming call, 2=SMS TX result)
# a[1..] = event-specific data
def modem_callback(a):
    if a[0] == 2:  # SMS TX result
        sms_id = a[1]
        tx_status = a[2]
        if tx_status == 1:
            status_text = "OK"
        else:
            status_text = "ERROR"
        print("SMS send result:")
        print("  ID     ->", sms_id)
        print("  Status ->", status_text)
        # ultra compact version
        # print("SMS send result -> ID:", a[1], "Status:", "OK" if a[2]==1 else "ERROR")
    else:
        # for now, ignore other events
        pass

# --- Register callback ---
sushi.cmd("set_modem_hnd", modem_callback)
print("Modem callback registered. SMS send results will be displayed here.\n")

# --- Send SMS ---
# Uncomment the next lines and change the number/text to test sending
# Alternative to avoid auto send at each script run: write the command 'sushi.cmd("send_sms"...' manually from the REPL
"""
res = sushi.cmd("send_sms", ("Hello from Sushi!", "123456789")) # replace "123456789" with destination number
if res[0] == 0:
    print("SMS command accepted, ID:", res[1])
else:
    print("Send SMS error:", res[0], "(", res[1], ")")
"""