#exponent function

# create a function that does this (2**3)

def raise_to_power(base_num, pow_num):
        result = 1
        for index in range(pow_num):
                result = result * base_num
        return result

input(raise_to_power(int(input()),int(input())))
