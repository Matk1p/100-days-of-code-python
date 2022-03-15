# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
num_students = 0 # challenge is to not use the len() / sum() function, hence the variables
for height in student_heights:
    total_height += height
    num_students += 1

print(round(total_height / num_students)) # intended results to show a rounded whole number



