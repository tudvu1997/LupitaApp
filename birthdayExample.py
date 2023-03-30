import json

pathToFile = "C:/Users/16692/Desktop/New folder (5)/birthday.json"

try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    exit(-1)

birthdayList = json.load(jsonFile)

birthdayDictionary = {}

for elem in birthdayList:
    name = elem["name"]
    birthday = elem["birthday"]
    birthdayDictionary[name] = birthday

name = input("Enter a name:")
print("name = " + name)
