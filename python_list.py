names = ["Mogos", "Henok", "Maharie", "Gerish"]
print("Hello ," + names[0])
print("Hello ," + names[1])
print("Hello ," + names[2])
print("Hello " + names[3])

fav_mode_transport = ["cars", "biycle", "Motor"]
print(f"I would like to own a Honda {fav_mode_transport[2]}")
print(f"I would like to own a Nissan {fav_mode_transport[0]}")
print(f"I would like to own a Olmo {fav_mode_transport[1].title()}")


# try it yourself 3-7
guests = ["Frezgie", "Ykealo", "Mehreteab", "Lisa"]
not_come = guests.pop(2)
# print(not_come)
new_comer = "Katrine"
guests.append(new_comer)
# print(guests)
guests.insert(1, "Mueller")
guests.insert(0, "Tedros")
guests.append("Yonas")
# print(guests)

# shrinking the list
invited_list = []
print(guests)
print(len(guests))
for invited in guests:
    if len(guests) > 3:
        guests.pop()


for rest in guests:
    guests.pop()
    invited_list.append(rest)


print(guests)
print(invited_list)


my_list = [1, 3, 4, 5]
print(sum(my_list))
