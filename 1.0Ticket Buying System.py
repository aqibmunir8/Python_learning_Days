name = input("Enter Your Name : ").title()
age = int(input("Enter Your age : "))
if 0<age<=3:
    print(f"{name}! Free to Use")
elif 3<age<=10:
    print(f"{name} Ticket Costs You 200")
elif 10<age<=60:
    print(f"{name} Ticket Costs You 300")
elif 60<age<140:
    print(f"{name} Ticket is Free For You too!")
elif age<=0 or age>=140:
    print("System Error")