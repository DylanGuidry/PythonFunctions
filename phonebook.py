#Phonebook
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
    'Kareem': '938-489-1234'
}

#Printing Elizabeth's phone number.
#Using .get:
print(phonebook_dict.get ("Elizabeth"))

#Adding an entry and printing number:
print(phonebook_dict.get ("Kareem"))

#Deleting Alice from existance:
del phonebook_dict["Alice"]
print(phonebook_dict)

#Changing Bob's phone number:
phonebook_dict["Bob"] == 968-345-2345
print(phonebook_dict.get ("Bob"))

#Printing all phone entries:
print(phonebook_dict)