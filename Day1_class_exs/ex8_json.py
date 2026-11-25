import json
devices = [
    {"hostname": "R1", "mgnt_ip":"10.0.0.1", "Reachable": "UP"},
    {"hostname": "R2", "mgnt_ip":"10.0.0.2", "Reachable":"UP",}
]

with open("inventory.json","w") as file:
    json.dump(devices, file, indent=2)

with open("inventory.json","r") as file:
    dev = json.load(file)
for device in dev:
    print("Hostname : ",device['hostname'])
    print("Mgmt IP: ",device["mgnt_ip"])

#handle malformed JSON using json.JSONDecodeError

try:
    with open("inventory.json","r") as file:
        dev = json.load(file)
    for device in dev:
        print("Hostname : ",device['hostname'])
        print("Mgmt IP: ",device["mgnt_ip"])
except json.JSONDecodeError:
    print("Error : inventory.json contains malformed JSON")


#
# import json

# with open("inventory.json", "w") as f:
#     f.write("""
# [
#   {
#     "hostname": "R1",
#     "mgnt_ip": "10.0.0.1",
#   }
# ]
# """)

# try:
#     with open("inventory.json", "r") as f:
#         devices = json.load(f)

# except json.JSONDecodeError as e:
#     print("JSON Error:", e)

# import json

# with open("inventory.json", "r") as file:
#     dev = json.load(file)

# for device in dev:
#     if "hostname" not in device or "mgnt_ip" not in device:
#         raise ValueError("Device is missing hostname or mgnt_ip")

#     print("Hostname:", device["hostname"])
#     print("Mgmt IP:", device["mgnt_ip"])