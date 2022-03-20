student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades ={}

#TODO-2: Write your code below to add the grades to student_grades.👇
def give_grade(score):

    if score >= 91: 
        return "Outstanding"
    elif score < 91 and score >= 81: 
        return "Exceeds Expectations"
    elif score < 81 and score >= 71:
        return "Acceptable"
    elif score < 71:
        return "Fail"
    else:
        return "Invalid Score"

for student in student_scores:
    student_grades[student] = give_grade(student_scores[student])    

# 🚨 Don't change the code below 👇
print(student_grades)