#!/usr/bin/env python3

# Dictionaries: A dictionary is a collection which is ordered, changeable, and does not allow duplicates. Fast because they use hashing, allow us to access a value quickly

capitals = {
    "Jawa Tengah": "Semarang",
    "Jawa Timur": "Surabaya",
    "Jawa Barat": "Bandung"
}

# print(capitals["Jawa Tengah"]) # Semarang
# print(capitals.get("Kalimantan Barat")) # None
# print(capitals.keys()) # dict_keys(['Jawa Tengah', 'Jawa Timur', 'Jawa Barat'])
# print(capitals.values()) # dict_values(['Semarang', 'Surabaya', 'Bandung'])
# print(capitals.items()) # dict_items([('Jawa Tengah', 'Semarang'), ('Jawa Timur', 'Surabaya'), ('Jawa Barat', 'Bandung')])

# capitals.update({"Kalimantan Barat": "Pontianak"}) # Add new items
# capitals.update({"Jawa Timur": "Ibukota Baru"}) # Change value

# capitals.pop("Jawa Barat")
# capitals.clear()

# for val in capitals: # Only for keys
#     print(val)


for key, val in capitals.items(): # keys with values 
    print(key + ": " + val)

