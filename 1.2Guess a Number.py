import random
win_num = random.randint(1,100)
print("Enter Your Number between 1 - 100")
coins = input("Enter Your Coins : ")
print("You Earned A Free Coin ;)")
ask = input("Enter your Guessing Number : ")
guess = 1
if "." in coins or "." in ask:
    print("You Losed all of your Coins,who said that to you Huh?")
else:   
    if ask and coins:
        coins = int(coins)
        ask = int(ask)
        for i in range(0,coins):
            if ask == win_num:
                print(f"You Win!! & You Guessed it {guess} times")
                break
            elif ask < 0:
                print("\nPlease Don't Enter Negative Numbers")
                print("Don't Waste Your Coins\n")
            elif ask >= 100:
                print("\nPlease Don't Enter Numbers Above Hunderd")
                print("You Are Wasting You Coins\n")
            else:
                if ask < win_num:
                    print("too Low")
                else:
                    print("too High")
            guess +=1
            ask = int(input("Enter You Guess Again : "))
        print(f"\nYou have {1+coins-guess}-Coins left")
    else:
        print("From your mistake, you lose all of your Coins ")
exit = input("Press any key from a to z and then Enter for Exit : ")
