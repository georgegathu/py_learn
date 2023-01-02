# Simple body temp Calculator using If elif else Statement
temperature = float(input("Enter your body temperature: "))
print("You have entered ", round(temperature, 2))

if temperature == 36:
    print("Normal temperature, don't panic.")
elif temperature > 36:
    print("You have a fever, seek medical attention!")
else:
    print("Below normal temperature, seek medical attention!")