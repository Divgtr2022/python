letter = '''Dear <|NAME|>,
Greetings from Divyanshu
I m happy to tell you about your selection
you are selected!

Date: <|DATE|>

'''
'''name = input("Enter your name \n") # program to insert values
date = input("Enter oyur date \n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)'''

'''you = letter.find("you") # program to find you in a given sentence
print(you)'''

'''about = letter.replace("you","hehe") # program to replace a word
print(about)'''

