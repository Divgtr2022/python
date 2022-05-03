sub1 = int(input("Enter the number of subject 1\n "))
sub2 = int(input("Enter the number of subject 2\n "))
sub3 = int(input("Enter the number of subject 3\n "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Your are fail")
elif((sub1+sub2+sub3)/3<40):
    print("You are fail due to total marsks less than 40.")
else:
    print("You have passed your examination.")