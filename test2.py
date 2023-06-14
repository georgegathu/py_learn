# BMI CHECKER 
weight = float(input('Enter weight in Kg: '))
height = float(input('Enter height in Meter: '))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight. Are you from Shakahola?")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are over weight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are Obese. wachana na food, Kula story sasa!")
else:
    print(f"Your BMI is {bmi} and you are clinically Obese. Kitakuramba!!")