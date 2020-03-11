glossary = {
    "list": "Listing objects ",
    "tuple": "Tuples  immutable",
    "if": "Testing condition ",
    "else": "else as default",
    "function": "Function  do more task",
    "elif": "if doesnt elif next",
    "add": "adding objects",
    "removing": "removing from list",
    "append": "adding objects to list",
    "delet": "is type of method"
}

for key, value in glossary.items():
    print(f"Key:{key.title()}")
    print(f"Value:{value.title()}")


# Rivers
rivers = {
    "nile": "Egypt",
    "Amazon": "Brazil",
    "Tekeze": "Sudan"
}
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

# looping on only keys
for key in rivers:
    print(key)

# looping only values
for value in rivers.values():
    print(value)


# Polling
favorite_language = {
    "jen": "Python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
course_addmi = ["sarah", "henok", "edward", "phil", "mogos"]
for name in course_addmi:
    if name in favorite_language:
        print(f"thanks {name.title()} for taking the course")
    else:
        print(f"Come {name.title()} take the course")


# Nesting dict in list or list in dict
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": "5", "speed": "slow"}
    aliens.append(new_alien)

# First 3 aliens change color to yellow and speeed to medium
for alien in aliens[:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = 10
print(aliens)
