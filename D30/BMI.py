height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")

BMI = weight / height ** 2
print(BMI)