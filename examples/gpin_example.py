# gpin_example.py [v20250929]

print("Testing GPIN...")

# --- Read initial input value ---
# sushi.cmd('read_gpin', idx) returns a tuple:
#   [0] = function result (0 = no error)
#   [1] = input value
myinput = sushi.cmd('read_gpin', 0)
if myinput[0] == 0:
    print("Value:", myinput[1])


# --- Callback executed when input status changes ---
def gpin_change_callback(source):
    """
    source = origin of the interrupt (0 = IO-Expander)

    Reads GPIN again and prints the value in binary if no error occurred.
    """
    if source == 0:
        v = sushi.cmd('read_gpin', 0)
        if v[0] == 0:
            print("GPIN value:", bin(v[1]))
        else:
            print("GPIN read error:", v[0])


# --- Register callback ---
sushi.cmd('set_gpin_int', gpin_change_callback)
