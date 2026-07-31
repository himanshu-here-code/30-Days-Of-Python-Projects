import json
import os

print("----WELCOME TO BMI COUNTER----")
name = str(input("Please Enter your Name: "))
gender = ["male","female"]
print("choose your gender")
for index,gender in enumerate(gender,1):
    print(f"{index}. {gender}")
gender_choose =int(input("Enter the number which defines your gender: "))
if gender_choose >2:
    print("please choose between 1 or 2")

elif gender_choose == 1:
    age =input("Please Enter your age sir: ")

elif gender_choose == 2:
   age =input("Please Enter your age ma'am: ")
else:
   print("input invalid. Try again.")

height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))

def bmi_calc(height , weight):
    height_in_m = height /100
    bmi = weight/height_in_m**2
    print(f"you bmi is {bmi:.2f}")
    return bmi
bmi = bmi_calc(height,weight)
person ={
    "name": name,
    "gender": gender,
    "age": age,
    "height": height,
    "weight": weight,
    "bmi": bmi
}
filename ="bmi_data.json"

if os.path.exists(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            data = []

    except json.JSONDecodeError:
        data = []
else:
    data = []

# Add new record
data.append(person)

# Save data
with open(filename, "w") as file:
    json.dump(data, file, indent=4)