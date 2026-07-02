
input_kg = float(input("How many kg you are? "))
input_height = float(input("How tall u are? "))
input_height = input_height / 100

h = input_height ** 2 

calculated = input_kg / h


if input_height == int:
    print("u need to separete 190 - 1.90")

if calculated < 18.5:
    print(f"You have index: {calculated:.2f}")
    print("You are underweigt ")

elif 18.5 <= calculated <= 24.9:
    print(f"You have index: {calculated:.2f}")
    print("You are ok")

elif 25.0 <= calculated <= 29.9:
    print(f"You have index: {calculated:.2f}")
    print("You are overweight")
    
else:
    print(f"You have index: {calculated:.2f}")
    print("You are obese")
    


