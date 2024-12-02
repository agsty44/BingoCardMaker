import random

bingoCard = []
usedNumbers = []

# initialise 2d array
for i in range(5):
    bingoCard.append([])

# loop through each row of the card
for i in range(5):
    # go up to 5 numbers
    for j in range(5):
        while True:
            newNum = random.randint(1, 100)
            if newNum not in usedNumbers:
                bingoCard[i].append(newNum)
                usedNumbers.append(newNum)
                break

for i in range(5):
    print(bingoCard[i])