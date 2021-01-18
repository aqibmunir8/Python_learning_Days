# A Program that only allow to watch COCO movie for those whose name starts with "A" and their age should be greater then 10, So You Are Allowed to Watch Coco Movie ;)
name = input("Enter Your Name : ").lower()
age = int(input("Enter Your Age : "))
if name[0]=="a" and age>10:
    print("You Can Watch Coco Movie!!")
else:
    print("You Can\'t Watch Coco Movie!!")
    ask = input("Do You Wanna Know WHy ( Y./ N. ): ").lower()
    if ask[0]=="y" and age> 10:
        print("Because the first Letter of your Name is not A")
        print("Sorry")
    elif ask[0]=="n" and age>18:
        print("As you wish")
    elif ask[0]=="n" and 0<age<18:
        print("Because You Are A KId, Sorry")
        print("Go outside, Play Games, Kido")