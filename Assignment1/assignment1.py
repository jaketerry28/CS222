## Assignment 1 

## part 1

# Calculate BMI
def calculateBMI(userWeight, userHeight):

    BMI = (userWeight * 703) / (userHeight ** 2)

    print("Your BMI is: " + str(round(BMI, 2)))

    if BMI < 18.5:
        print("You are underweight.")
    elif 18.5 <= BMI < 24.9:
        print("You are normal weight.")
    else:
        print("You are overweight.")

# Get user weight and height
userWeight = float(input("Enter your weight in lbs: "))
userHeight = float(input("Enter your height in inches: "))

print("Your weight is: " + str(userWeight) + " lbs")
print("Your height is: " + str(userHeight) + " inches")

calculateBMI(userWeight, userHeight)

## part 2

def sumEvenNumbers():
    sum = 0
    # for all even numbers from 1 to 100
    for i in range (2, 101, 2):
        sum += i
        print(f"sum is: {sum}")
    print("The sum of even numbers from 1 to 100 is: " + str(sum))
    
sumEvenNumbers()

## part 3

def sumOddNumbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    sum = 0

    # check which number is smaller
    if a < b:
        for i in range (a, b + 1):
            if i % 2 != 0:
                sum += i
                print(f"sum is: {sum}")
        print("The sum of odd numbers from " + str(a) + " to " + str(b) + " is: " + str(sum))

    else:
        for i in range (b, a + 1):
            if i % 2 != 0:
                sum += i
                print(f"sum is: {sum}")
        print("The sum of odd numbers from " + str(b) + " to " + str(a) + " is: " + str(sum))
        
sumOddNumbers()

## part 4

def sellStock():
    targetPrice = float(input("Enter target price: "))
    currentPrice = float(input("Enter current price: "))

    if currentPrice >= targetPrice:
        print("Shares can be sold now.")
    else:
        print("Shares cannot be sold now.")

sellStock()

## part 5

def projectedTuition():
    tuition = 8000
    print(f"Initial tuition: ${tuition:.2f}")
    for i in range(5):
        tuition += (.03 * tuition)
        print(f"Year {i + 1} projected tuition per semeseter: ${tuition:.2f}")

projectedTuition()