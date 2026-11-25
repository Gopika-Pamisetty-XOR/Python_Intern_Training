vlanID = input("Enter vlan ID:  ")
vlanID = int(vlanID)
if not 1<= vlanID <= 4094:
    raise ValueError("vlanId must be in between 1 and 4094")

print("Valid vlanID : ",vlanID)
