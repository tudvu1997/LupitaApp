import json

pathToFile = "C:/Users/jerom/Documents/GitHub/class-python/birthday/birthday.json"

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

    print("name = " + name)
    print("birthday = " + birthday)

    birthdayDictionary[name] = birthday

print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])

name = input("Enter a name:")
print("name = " + name)
