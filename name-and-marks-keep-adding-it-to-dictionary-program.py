marks = {}
subject_count = int(input("enter how many subject = "))
for i in range(0,subject_count):
    subject_name = input("enter subject name = ")
    subject_marks = int(input(f"enter marks for {subject_name} = "))
    marks[subject_name] = subject_marks
print(marks)