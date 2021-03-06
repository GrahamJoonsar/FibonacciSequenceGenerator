fNumbers = [1, 1]

for i in range(101):
    fNumbers.append(fNumbers[-1] + fNumbers[-2])

print(fNumbers)
