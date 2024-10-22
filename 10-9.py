first_name = "Mark"
last_name = "Josh"
age = 50
gpa = 3.3022

print("Your full name is " + first_name + " " + last_name + ". Your age is " + str(age) + ". " + "Your gpa is " + str(round(gpa, 1)))

print(f"Your full name is {first_name} {last_name}, your age is {age}, your gpa is {gpa:.2f}")

print("full name\t\tage\t\tgpa")
print(f"{first_name} {last_name} {str(age):>10s} {str(gpa):>10s}")
