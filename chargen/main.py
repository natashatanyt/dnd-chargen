import random

#ro
def RollStats():
    dice = []

    for i in range(4):
        dice.append(random.randrange(1,7))

        dice.sort()

    total = 0

    for i in range(1, 4):
        total += dice[i]
    
    return total

stats = []
for i in range(6):
    stats.append(RollStats())

stats.sort(reverse=True)
print("Stats:", *stats)