import random
import data

#class to store character info
class Character:
    c_recStat = []
    c_class = ""
    c_weapon = []
    c_armour = []
    c_hp = 0



#rolls stats 
def RollStats():
    dice = []

    for i in range(4):
        dice.append(random.randrange(1,7))

        dice.sort()

    total = 0

    for i in range(1, 4):
        total += dice[i]
    
    return total

def charCreation():
    #stats
    #creates an array and stores values for stats
    stats = []
    for i in range(6):
        stats.append(RollStats())
    #sorts stats in decreasing order and prints
    stats.sort(reverse=True)
    print("Stats:", *stats)

    #creates class to store character data
    newChar = Character()

    #chooses and prints class for the character
    classes = []

    for _class in data.classes:
        classes.append(_class)

    newChar.c_class = classes[random.randrange(0, len(classes))]
    print ("Class:", newChar.c_class)

    #depending on the class, the primary ability, hit dice, and HP are also printed
    for type in data.classes:
        if newChar.c_class == type:
            print("Recommended Primary Ability:", data.classes[newChar.c_class]['Stat'])
            print("Saving Throw Profiencies:", data.classes[newChar.c_class]['Saving Throws'])
            print("Hit Dice:", data.classes[newChar.c_class]['Hit Dice'])
            print("HP:", data.classes[newChar.c_class]['HP'], "+ Constition Modifier")
            

#main function
user_input = ""

while user_input != "n":
    user_input = input("Create Character? (Y/N): ").lower()

    if user_input == 'y':
        charCreation()

        #divider
        print ("---------------------------")
    
    #ends char creation
    elif user_input == 'n':
        print("Ending Character Creation.")

    #invalid input
    else:
        print("Invalid Input. Try Again.")





