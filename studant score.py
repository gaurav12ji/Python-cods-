student_score = {"Herry":81,
                 "Ron":78,
                 "Hermione":99,
                 "Draco":74,
                 "Nevile":62,
                 "Gaurav":99,
                 "Aditya":32}
student_grade = {}

for Student in student_score:
    score = student_score[Student]
    if score >= 90:
        student_grade[Student] = "A+"
    elif score >= 60 and score < 90:
        student_grade[Student] = "A"
    elif score >= 50 and score < 60:
        student_grade[Student] = "B"
    elif score >= 45 and score < 50:
        student_grade[Student] = "C"
    else:
        student_grade[Student] = "Fail"
print(student_grade)



