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

#
first_name = "Medhanie"
last_name = "Desale"
print("my name is {} {}".format(first_name, last_name))
print(first_name.upper() + " " + last_name.upper())
print(first_name.lower() + " " + last_name.lower())
# casefold
name = "Müller"
print(name.casefold())
# center
# print(first_name.center(width[,fillchar]))
# count
print(first_name.count("e"))
# encode
print(first_name.encode())
# slicing
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

print(verse)
print("\n The length of the sentence is: {} ".format(len(verse)))
print("The index of first occurence of and {}: ".format(verse.index("and")))
print(verse.rfind("you"))
print("The number of you in the sentence {}: ".format(verse.count("you")))

print(list(range(0, -5)))
# for loop with html tags
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li> {} </li> \n".format(item)

html_str += "</ul>"


print(html_str)

# word frequency with dict
book_title = ["great", "expectation", "the", "adventures", "of", "sherlock",
              "holmes", "hamlet", "huckleberry", "fin", "gasby", "the", "sherlock"]
word_counter = {}
for word in book_title:
    if not word in word_counter:
        word_counter[word] = 1

    else:
        word_counter[word] += 1

print(word_counter)
# sentence
sentence = "The black panter has been very famous during the last summer and has been watched through out the world"
# finding words how many times repeated
list_of_sentence = sentence.title().split()
print(list_of_sentence)

freq_word = {}
for word in list_of_sentence:
    if word not in freq_word:
        freq_word[word] = 1
    else:
        freq_word[word] += 1

print(freq_word)
