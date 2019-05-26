#list functions

lucky_numbers = [3, 35, 19, 9, 46]
friends = ["Inderpreet", "Jasmin", "Gurbeer", "Bharat", "Tejpaul"]
print(friends)

friends.extend(lucky_numbers) # adds the other lists on top of another
print(friends)

friends.append("Mahaakaal")
print(friends)

friends.insert(1, "Simran")
print(friends)

friends.remove("Tejpaul")
print(friends)

friends.pop() #removes last element
print(friends)

print(friends.index("Gurbeer"))

print(friends)

print(friends.count("Gurbeer"))

friends2 = friends.copy()

print(friends2)


