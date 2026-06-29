#fitness calculator version 2 (Calculates BMR, TDEE, Protein Goal)

# 1.BMR calculation
'''FORMULA: 
Mifflin-St Jeor Formula (most commonly used)
For men: BMR=(10*weight in kg)+(6.25*height in cm)-(5*age)+5
For women: BMR=(10*weight in kg)+(6.25*height in cm)-(5*age)-161'''

import sys

weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
gender = input("Select your gender(M/F): ")

if gender == "M" or gender == "m":
    BMR=(10*weight)+(6.25*height)-(5*age)+5
elif gender == "F" or gender == "f":
    BMR=(10*weight)+(6.25*height)-(5*age)-161
else:
    print("Invaild gender input. TRY AGAIN!")
    sys.exit()

# 2.TDEE calculation
'''FORMULA: TDEE=BMR*Activity Factor'''
#taking activity level as input would be convinient for user

activity_level = int(input("What is your activity level?\n1 - Sedentary (little/no exercise)\n2 - Light exercise (1–3 days/week)\n3 - Moderate exercise (3–5 days/week)\n4 - Heavy exercise (6–7 days/week)\nSelect your level and type a number between(1-4): "))
match activity_level:
    case 1: TDEE = BMR * 1.2
    case 2: TDEE = BMR * 1.3
    case 3: TDEE = BMR * 1.5
    case 4: TDEE = BMR * 1.7
    case _: print("Invaild activity level input. TRY AGAIN!"), sys.exit()

# 3.Protein goal calculation
'''FORMULA: Protein (g/day)=Weight (kg)*Protein Multiplier'''
#taking fitness goal as input would be convinient for user

fitness_goal = int(input("What is your fitness goal?\n1 - General fitness\n2 - Muscle gain\n3 - Fat loss\nSelect your goal and type a number between(1-3): "))
match fitness_goal:
    case 1: protein = weight * 1.4
    case 2: protein = weight * 1.9
    case 3: protein = weight * 2.1
    case _: print("Invaild fitness goal input. TRY AGAIN!"), sys.exit()

#Final Output
print()
print("--Your Result--")
print()
print("Basic Metabolic Rate =",BMR,"calories/day")
print("Maintenance Calories =",TDEE,"calories/day")
match fitness_goal:
    case 1: protein = weight * 1.4, print("You should eat at your maintenance calories with",protein,"grams of protein per day.")
    case 2: protein = weight * 1.9, print("You should eat at a 200-400 caloric surplus from your maintenance calories with",protein,"grams of protein per day.")
    case 3: protein = weight * 2.1, print("You should eat at a 200-400 caloric deficit from your maintenance calories with",protein,"grams of protein per day.")
