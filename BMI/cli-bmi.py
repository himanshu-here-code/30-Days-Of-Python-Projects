import json
import os

print("----WELCOME TO BMI COUNTER----")
name = str(input("Please Enter your Name: "))
genders = ["male", "female"]

for index, g in enumerate(genders, 1):
    print(f"{index}. {g}")

gender_choose = int(input("Enter the number: "))

if gender_choose in (1, 2):
    gender = genders[gender_choose - 1]

    if gender == "male":
        age = float(input("Please Enter your age sir: "))
    else:
        age = float(input("Please Enter your age ma'am: "))
else:
    print("Invalid choice.")
    exit()

height = float((input("Please enter your height in cm: ")))
weight = float(input("Please enter your weight in kg: "))

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
folder ="BMI/bmi_data.json"

if os.path.exists(folder):
    try:
        with open(folder, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            data = []

    except json.JSONDecodeError:
        data = []
else:
    data = []

data.append(person)

with open(folder, "w") as file:
    json.dump(data, file, indent=4)