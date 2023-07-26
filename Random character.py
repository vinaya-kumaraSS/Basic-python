import random
r_int = random.randrange(1, 27)
print(r_int)
r_char = chr(64 + r_int) if r_int > 0 else 'Z'
print(r_char)