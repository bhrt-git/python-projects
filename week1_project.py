#Personal fitness calculator(calculates BMR, TDEE and Protein Goal)

#Calculating BMR
'''Formula:
Mifflin-St Jeor Formula (most commonly used)
For men: BMR=(10×weight in kg)+(6.25×height in cm)−(5×age)+5
For women: BMR=(10×weight in kg)+(6.25×height in cm)−(5×age)−161'''

import sys

weight = float(input("Enter your weight(in kgs): "))
height = float(input("Enter your height(in cm): "))
age = int(input("Enter your age(in years): "))
gender = input("Enter your gender(M/F): ")

if gender == "M":
    BMR=(10*weight)+(6.25*height)-(5*age)+5
elif gender == "F":
    BMR=(10*weight)+(6.25*height)-(5*age)-161
else:
    print("Invalid gender, choose type either M or F")
    sys.exit()
print("BMR =",BMR,"calories/day")
print("\n")

#Calculating TDEE
'''Formula:
TDEE=BMR×Activity Factor'''

activity_level = int(input("Select your activity level\n1 - Sedentary (little/no exercise)\n2 - Light exercise (1-3 days/week)\n3 - Moderate exercise (3-5 days/week)\n4 - Heavy exercise (6-7 days/week)\n5 - Athlete/very active\nSelect one of the five types(1-5): "))
match activity_level:
    case 1:
        TDEE=BMR*1.2
    case 2:
        TDEE=BMR*1.375
    case 3:
        TDEE=BMR*1.55
    case 4:
        TDEE=BMR*1.725
    case 5:
        TDEE=BMR*1.9
    case _:
        print("Invalid activity level choose and type a number(1-5)")
        sys.exit()
print("TDEE=",TDEE,"calories/day")
print("\n")

#Calculating Protein Goal
'''Formula:
Protein (g/day)=Weight (kg)×Protein Multiplier'''

fitness_goal = int(input("Select your fitness goal\n1 - General Fitness\n2 - Muscle Gain\n3 - Fat Loss\nSelect one of the three types(1-3): "))
match fitness_goal:
    case 1:
        PrI=weight*1.4
    case 2:
        PrI=weight*1.9
    case 3:
        PrI=weight*2.1
    case _:
        print("Invalid fitness choose and type a number(1-3)")
        sys.exit()
print("Protein Intake =",PrI,"g/day")
print("\n")

#Final Evaluation
print("YOUR FITNESS EVALUATION IS AS FOLLOWS: ")
print("Based on your provided information, activity levels and fitness goals-")
print("Your Basal Metabolic Rate is",BMR,"calories/day.")
print("Your body needs",TDEE,"calories/day to maintain its current weight.")
match fitness_goal:
    case 1:
        print("-eat at the maintenance calories for general fitness/maintain your weight.")
    case 2:
        print("-eat at 300-500 caloric surplus from maintenance calories for muscle gain.")
    case 3:
        print("-eat at 300-500 caloric deficit from maintenance calories for fat loss.")
print("Your body needs around",PrI,"g of protein per day for your desired goal.")