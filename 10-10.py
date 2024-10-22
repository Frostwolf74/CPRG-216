name_list = ["mark", "josh", "david"]
gpa_list = [3.5, 3, 4]

for i in range(0, len(name_list)):
    print(name_list[i] + ": " + str(gpa_list[i]))


student_dict = {"mark":3.5, "josh": 4, "david":4}

print(student_dict["mark"])

for student in student_dict:
    print(student_dict[student])