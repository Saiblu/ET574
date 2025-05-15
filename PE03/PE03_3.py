height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

height_m = height_cm / 100

bmi = weight_kg / (height_m **2)

print(f"BMI: {bmi: .3f}")