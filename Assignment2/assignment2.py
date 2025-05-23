# Assignment 2

'''
hot dogs = 10 per pack
buns = 8 per pack

The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over
The number of hot dog buns that will be left over
'''

def hotDogCounter():
    persons  = int(input("Enter how many people will be attending: "))
    hotdogs = int(input("Enter how many hotdogs each person gets: "))

    hotdogsPerPerson = persons * hotdogs

    # divmod returns a tuple of (quotient, remainder)
    buns = divmod(hotdogsPerPerson, 8) # total buns / 8
    weiners = divmod(hotdogsPerPerson, 10) # total weiners / 10

    if buns[1] > 0:
        bunPacks = buns[0] + 1
        print(f"Total hotdog bun packs needed: {bunPacks}")
        print(f"Remaining buns: {8 - buns[1]}")
    else:
        print(f"Total hotdog bun packs needed: {buns[0]}")
        print(f"No remaining buns")

    if weiners[1] > 0:
        weinerPacks = weiners[0] + 1
        print(f"Total hotdog packs needed: {weinerPacks}")
        print(f"Remaining buns: {10 - weiners[1]}")
    else:
        print(f"Total hotdog packs needed: {weiners[0]}")
        print(f"No remaining weiners.")
        

hotDogCounter()