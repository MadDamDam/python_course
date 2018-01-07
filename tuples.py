#Tuples are lists you can not change, which makes them fast to go through.

#init a Tuple
constant_vals = ()
constant_vals = (39,)
type(constant_vals)
constant_vals = ("Jack","Arizona",9,"Atlanta",4,6,9)

#get number of members
len(constant_vals)

#count member in Tuple
constant_vals.count(9)

#get location of member in tuple
constant_vals.index("Atlanta")

#Check if value in Tuple
"Texas" in constant_vals

#Run over members in Tuple
for val in constant_vals:
    print val
