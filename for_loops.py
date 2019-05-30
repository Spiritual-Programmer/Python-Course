#for loops
print("ex.1")
for letter in  "Giraffe Academy":
        print(letter)

print("\nex.2")
friends = ["Jim", "Karen", "Kevin"]
for friend in  friends:
        print(friend)

print("\nex.3")
for index in  range(10):
        print(index)

print("\nex.4")
for index in  range(3, 10):
        print(index)

print("\nex.5")
for index in  range(len(friends)):
        print(friends[index])

print("\nex.6")
for index in  range(5):
        if index == 0:
                print("first Iteration")
        else:
                print("Not first")
