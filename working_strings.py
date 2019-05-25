#working with strings and functions

phrase = "Giraffe Academy"

#can use \ to add " or other texts
#\n starts text on next line

#concatenation(adding or appending on) with strings
print(phrase + " is cool, plus me concatening strings")

#functions

print("converting string into uppercase letter")
print(phrase.upper)
print("Now converting string to lowercase ")
print(phrase.lower)
print(phrase.isupper())#Checking if value is true or false of uppercase letters
print(phrase.upper().isupper()) #combining 

print(len(phrase)) #length in phrase
print(phrase[0]) #getting index of character
print(phrase.index("r"))   #index: tells us where the character is, passing parameters
print(phrase.replace("Giraffe","Singh"))
