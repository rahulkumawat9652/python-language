student_data = {"student1":[67,87,90,78,89],
                "student2":[77,80,70,90,69],
                "student3":[87,77,80,75,89],
                "student4":[97,87,96,70,99],
                "student5":[78,67,97,96,95]}
for name,marks in student_data.items():
    total = sum(marks)
    percentage = total/500*100
    print(f"{name} has scored total {total} marks, percentage = {percentage:0.2f}") 