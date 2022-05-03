num = int(input("Enter the number here :\n"))
for i in range(1,11):
    print(str(num) +  "x" + str(i) + "=" + str(num*i))#Method no 1

    #or

    print(f"{num}+{i}={num*i}") #Method no 2

    #Through while loop

num = int(input("Enter the name here: \n"))
i = 1
while i<=10:
        print(str(num) +  "x" + str(i) + "=" + str(num*i))
        i = i+1

# Multiplication using def
def multiply(num):
    for i in range(1,11):
        print( str(num) + "x" + str(i) + "=" + str(num*i))
n = int(input("Insert the number here :\n"))
print(multiply(n))
 

       