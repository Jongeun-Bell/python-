from functools import partial

def power(base,exponent,multiplier):
    return base ** exponent * multiplier

print(power(3,2,4))

square_and_double = partial(power,2,multiplier=3)
print(square_and_double(4))