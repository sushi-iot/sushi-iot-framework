# gpin_example.py [v20250929]

"""
Example: Read IO-Expander input and detect changes via interrupt callback.
Each sushi.cmd(...) call returns a tuple:
    [0] = function result (0 = no error)
    [1] = input value or error message if err ≠ 0
"""

print("Testing GPIN...\n")


# --- Read initial input value ---
myinput = sushi.cmd('read_gpin', 0)
if myinput[0] == 0:
    print("Initial GPIN value:", bin(myinput[1]))
else:
    print("Read GPIN error:", myinput[0], "(", myinput[1], ")")


# --- Callback executed when input status changes ---
# source = origin of interrupt (0 = IO-Expander)
def gpin_change_callback(source):
    # read GPIN again and print in binary
    if source == 0:
        v = sushi.cmd('read_gpin', 0)
        if v[0] == 0:
            print("GPIN value:", bin(v[1]))
        else:
            print("GPIN read error:", v[0], "(", v[1], ")")


# --- Register callback ---
sushi.cmd('set_gpin_int', gpin_change_callback)
print("\nCallback registered. Change the input and see the output.")