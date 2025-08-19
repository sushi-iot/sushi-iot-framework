# TEST GPIO
print("Testing GPIN...")
g = sushi.cmd('read_gpin' , 0)
print("Value:" , g[1])

def gpin_change_callback(source):
    if source == 0:	#source is IO-Expander
        v = sushi.cmd('read_gpin' , 0)
        if v[0] == 0:		#no errors occured
            print("GPIN value:" , bin(v[1]))	#print the input value in binary
        else:
            print("GPIN read error:" , v[0])

sushi.cmd('set_gpin_int' , gpin_change_callback)