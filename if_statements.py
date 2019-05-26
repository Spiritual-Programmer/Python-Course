#Writing if statements

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")
    print("You are a female")

is_tall = True

if is_male or is_tall:
    print("You are male, tall or both")
else:
    print("You are neither male or tall")


if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You not a male but are tall")
else:
    print("You are not male and not tall")

