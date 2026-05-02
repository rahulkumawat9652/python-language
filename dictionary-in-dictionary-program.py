student_data = {
       "rahul":{"roll_number":122,"gender":"male","marks":[67,89,90,98,67]},
        "shiv":{"roll_number":123,"gender":"male","marks":[67,90,99,98,77]},
        "rakesh":{"roll_number":124,"gender":"male","marks":[67,79,90,88,77]}
        }
for name,details in student_data.items():
    print(name)
    print(details)
    print(details["marks"])
    print(sum(details["marks"])) 