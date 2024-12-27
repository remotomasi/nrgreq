#!/usr/bin/python3 
      #----------------------------------------------------------------------------
      # Created By  : Remo Tomasi 
      # Created Date: 25/12/2024 
      # version ='0.1'
      # ---------------------------------------------------------------------------

# Ask to the user to input values
weight_kg = float(input("Insert your weight in kg: "))
height_cm = float(input("Insert your height in cm: "))
age = int(input("Insert your age: "))
activity_level = float(input("Insert your activity level (i.e. 1.2, 1.375, 1.55, 1.725, 1.9): "))
'''
    ACTIVITY LEVELS:

    Sedentary (little or no exercise):
    Activity level = 1.2

    Slightly active (light exercise or light physical activity 1 to 3 days a week):
    Activity level = 1.375

    Moderately active (moderate exercise or light physical activity 1 to 3 days a week):
    Activity level = 1.55

    Very active (vigorous exercise or light physical activity 6 to 7 days a week):
    Activity level = 1.725

    Extremely active (very intense physical activity, physical labor or training twice a day, etc.):
    Activity level = 1.9
'''

# BMR calculus (Harris-Benedict per uomini)
BMR = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)

# TDEE calculus
TDEE = BMR * activity_level
print(f"Your TDEE is: {round(TDEE)} kcal")

# Create space
print(f"")
