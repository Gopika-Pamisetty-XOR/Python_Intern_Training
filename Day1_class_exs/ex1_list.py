interfaces = ["eth0", "eth1", "eth2", "eth3", "eth4", "eth5"]
interfaces.append("eth6")
interfaces.remove("eth5")
print("First Interface :    ",interfaces[0])
print("last Interface :    ",interfaces[-1])
print("Total count: ",len(interfaces))

