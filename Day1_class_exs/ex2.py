network = {
    "device1": {"hostname": "R1", "mgnt_ip":"10.0.0.1", "status": "UP"},
    "device2" : {"hostname": "R2", "mgnt_ip":"10.0.0.2", "status": "down", "location":"BLR"}
}

print(network)

for device in network.values():
    print(device)
    device["platform"] = "9k"

print(network)

for device,details in network.values():
    print(device)
    for key,value in value.details():
        print(key,":",value)