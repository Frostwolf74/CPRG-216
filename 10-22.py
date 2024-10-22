# function that takes an integer, doubles it then returns it

def double_number(number):
    new_number = number*2
    return new_number

num = input("Enter number: ")

print(double_number(int(num)))