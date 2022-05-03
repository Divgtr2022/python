#To find the name in a given list
names = ["rohan", "anushka","divyanshu","manas","arushi","sachin","satyankar"]
name = input("Enter the name: \n")

if(name in names):
    print("Your name is pesent in the list")
else:
    print("Your name is not present in the list")