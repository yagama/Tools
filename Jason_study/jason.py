import os
import json

#load var from jason
Config = json.load(open("example.json"))

#print all 
#print(Config)

#print var from Config
print(Config["Platform"])

#Modify
#Config["Platform"] = "XBOX"

#Print it again
#print(Config["Platform"])

#write back to json, you can check jason file later
#json.dump(Config, open("example.json", "w"), sort_keys=False, indent=4, separators=(",", ": "))