#Spam detector


text = input("Enter the text here : \n")

if("makes a lot of money" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam.")
else:
    print("This is not a spam.")
