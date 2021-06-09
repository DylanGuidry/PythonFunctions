#Dictionaries are defined with {}
friend = {
    #They have keys/ values pairs
    "name": "Alan Turing", 
    "Cell": "1234567",
    "birthday": "Sep. 5th"
}

#Empty dictionary
nothing = {}

#Values can be anything

suoerhero = {
    "name": "Tony Stark",
    "Number": 40,
    "Avenger": True,
    "Gear": [
        "fast car",
        "money",
        "iron suit",
    ],
    "car": {
        "make": "audi",
        "model": "R8"
    },
    "weakness": "his ego"
}

#Get values with key names:
print(suoerhero)
#Get method also works, and can have a "fallback"
print(suoerhero.get("name", "Uknown"))
#Access to all values aof all keys:
print(suoerhero.values())
#Searching for a keys in a dictionary:
if "weakness" in suoerhero:
    print("bad guys might win")
else:
    print("bad guys go home")
#Updating values:
suoerhero["avenger"] == "fartbutt"
print(suoerhero)
#Deleting from a dictionary:
del suoerhero["gear"]

#Accessing data:
print(suoerhero["name"])
for item in suoerhero["Gear"]:
    print(item)

# for key, value in suoerhero:items():
#     print(f"Suoerhero's {key} is")
#     print(value)