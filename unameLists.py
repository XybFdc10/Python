from itertools import product

uname = "admin"

result = []

for combo in product([0, 1], repeat=len(uname)):
    temp = ""
    for i, bit in enumerate(combo):
        if bit == 0:
            temp += uname[i].lower()
        else:
            temp += uname[i].upper()
    result.append(temp)

for r in result:
    print(r)
