#write apython program that take a person,age and categoriesit as:

age = int(input("enter your age"))
if age<13:
    print("categories of child age")
elif (13<19):
    print("categories of teen age")
elif (20-59):
    print("categories of adult age")
elif age >= 60:
    print("categories of senior")
else:
    print("invaliad age")
