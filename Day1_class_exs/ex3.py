conf = "interface Ethernet1/1, admin=up, vlan=200"
conf = conf.strip()
print(conf)


parts = conf.split(",")
print(parts)

interface_name = parts[0].strip().split()[1]
admin = parts[1].strip().split("=")[1].strip()
vlan_value = parts[2].strip().split("=")[1].strip()

print("Interface Name:", interface_name)
print("Admin:", admin)

try:
    vlan = int(vlan_value)
    print("VLAN:", vlan)
except ValueError:
    print(f"Error: VLAN '{vlan_value}' is not a valid numeric VLAN ID")