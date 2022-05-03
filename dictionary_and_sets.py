myDict = {
    "pankha": "fan",
    "kambal" : "blanket",
    "sadak" : "road"
}
print("Options are :",  myDict.keys)
a = input("Enter the hindi word : ")
print("The meaning of your hindi word is : ", myDict.get(a) )