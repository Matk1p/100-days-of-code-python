from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# using list comprehension with dictionaries
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items if test}
# get a new dictionary that takes in student names as key and a random score as the value
student_scores = {student: randint(1, 100) for student in names}

# getting only the students that passed
passed_students = {student: student_scores[student] for student in student_scores if student_scores[student] >= 60}
print(student_scores)
print(passed_students)

# alternatively --> cleaner
passed_students_2 = {student: score for (student, score) in student_scores.items() if score >= 60}
print(student_scores)
print(passed_students_2)