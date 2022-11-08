# Marcos Valencia
#11/7/2022
# This program will determine where a student should be placed with the gpa they have

lastname = input("Enter Last name")
while lastname != "ZZZ":
    firstname = input("Enter First name")
    GPA = float(input("Enter GPA"))
    if GPA >= 3.5:
        print("{} {} has made the dean list.".format(firstname, lastname))
    else:
        if GPA >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname)) 
    lastname = input("\nEnter Student Last Name: ")
   
