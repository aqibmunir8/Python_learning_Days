#finding Project
print("Findig Project \n")
ask = input("Enter Your Sentence : ").lower()
find = input("Enter your Word or Words to Wanna Find : ").lower()
find_1 = ask.find(find)
find_2 = ask.find(find,find_1 + 1)
print(find_1)
print(find_2)
print(f"The Sentence You Entered : \"{ask.title()}\" ")
Exit = input("press between A to Z and then Enter for Exit : ")

