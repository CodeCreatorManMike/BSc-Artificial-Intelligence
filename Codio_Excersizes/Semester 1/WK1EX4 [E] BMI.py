"""Can i write a program that readss a persons weight & height and outputs their body mass index (weight divided by height squared)
enter weight in kg, and height in cm.... weight/(height/100)**2
"""

# collect users weight in kg's
# its important to keep in mind that both of these individual variables could also be float values and will output a float value (users might be 84.5 kgs for example)
# EG: 85
weight = float(input("\nWhat is your weight in Kilograms (KG)?"))


# collect users height in cm's
# its important to keep in mind that both of these individual variables could also be float values and will output a float value
# EG: 182.88
height = float(input("\nWhat is your height in Centre meters (CM)?"))


# in both examples i've made use of (float()) function, to pre set the values as float values to avoid any errors

# bmi needs to be initialized with the equation to reach its own conclusion
bmi = float(weight / (height/100)**2)

# BMI reporting message:
bmi_reporting_message = f"\nYour BMI is {bmi}"

print(bmi_reporting_message)



"""
extra functionality this program could have:
-> grouping users by there weight/bmi category:

-> this groups each and assigns a category to users depending on what their bmi is

if bmi < 18.5:
  category = "underweight"
elif bmi < 25:
  category = "healthy weight"
elif bmi < 30:
  category = "overweight"
elif bmi < 35:
  category = "obesity class 1"
elif bmi < 40:
  category = "obesity class 2"
else:
  category = "obesity class 3"

print(f"Your BMI is {bmi:.2f}. Your category is {category}.")

: indicates formatting instructions
.2f here indicates the decimal points that should be presented (f - format it as a floating point number)

"""