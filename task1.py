# Module 6: Data Structures and Strings in Python
#
# Task 1: Create a Dictionary of Student Marks
#
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.



student_marks = {
    "karan" : 75,
    "nilesh" : 90,
    "mayur" : 85,
    "keval" : 80
}

student = input("Enter your name: ")
student_name = student.lower()

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"The marks of {student_name} is {marks}")
else:
    print(f"Student {student_name} does not exist")