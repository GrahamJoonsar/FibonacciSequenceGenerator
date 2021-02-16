fNumbers = [1, 1]

for i in range(101):
    fNumbers.append(fNumbers[(len(fNumbers)-1)] + fNumbers[(len(fNumbers)-2)])

print(fNumbers)