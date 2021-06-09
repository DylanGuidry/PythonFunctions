#Example given:
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
    'name': 'Jasmine',
    'email': 'jasmine@yahoo.com',
    'interests': ['photography', 'tennis']
        },
        {
    'name': 'Jan',
    'email': 'jan@hotmail.com',
    'interests': ['movies', 'tv']
        }
    ], "friendcounter": 0
}

#Getting email address from Ramit:
# print(ramit.get("email"))

# #Getting Ramit's interest:
# print(ramit.get("interests"))

# #Getting email of Jasmine:
# print(ramit["friends"][0]["email"])

# #Getting Jan's second interest:
# print(ramit["friends"][1]["interests"][1])

#Friends Counter:
# def numberfriends():
#     counter = 0
#     for friendnumber in ramit["friends"]:
#         counter += 1
#     ramit["friendcounter"] = counter

# numberfriends()
# print (ramit["friendcounter"])

# #Letter Summary:
# letterslist = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
# "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "p": 0, "q": 0, "r": 0, "t": 0, "u": 0,
# "u": 0, "w": 0, "x":0, "y": 0, "z": 0 }

# user_word = str(input("Input word here:"))

# def letters_dict(user_word):
#     for letter in user_word:
#         if user_word in letterslist:
#             letterslist[letter] += 1

# letters_dict("letterslist")

# def greeting(name):
#     print(f"Hello {name}")

# greeting("Dylan")

# list_numbers = [4, 8, 10, 15]

#Function:
def greeting(company_name):
    print(f"Hello {company_name}")

greeting("Google")
greeting("Hulu")

#Returning Function:
def get_greeting(company):
    return f"Hi {company}"

message = get_greeting("Google")