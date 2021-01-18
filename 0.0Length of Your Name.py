#Count Project 
print("A.M. Services")
name = input("Enter your Name : ").replace(" ","")
word = input("Enter your Word : ").replace(" ","")
length = len(name)
count = name.lower().count(word.lower())
print("Length of your name is : " + str(length))
print("Counted Word in Your Name is : " + str(count))
print("Thanks for using Our Services")

exit = input("\nPress any key from A to Z and Then Enter For Exit : ")