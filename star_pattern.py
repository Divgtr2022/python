#Star pattern 1
n = 3
for i in range(3):
   print(" " * (n-i-1), end="")
   print("*" * (2*i+1), end="")
   print(" " * (n-i-1))

#Star pattern 2
length = int(input("Enter the side of square :"))

for i in range(length):
    for j in range(length):
        if(i==0 or i==length - 1 or j==0 or j==length - 1):
            print("*" , end="")
        else:
            print(" " , end="")
    print()

   