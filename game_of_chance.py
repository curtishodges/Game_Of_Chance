import random
def play_again():
        while True:
            reply = input("Would you like to contiune? y or n ")
            if reply not in {"y", "n"}:
                print("Please enter valid input")
            elif reply == "n":
                return "Thank you, bye!"
                break
            elif reply == "y":
                return coin_flip(money)

def coin_flip(money):
        new_money_value = money
        # Ensures a heads of tails option is selected
        while True:
            try:
                guess = input("Heads or Tails? ")
                if guess not in {"Heads", "heads", "Tails", "tails"}:
                    print("Please enter heads or tails")
                else:
                    break
            except ValueError:
                print("Please choose heads or tails")
                continue
        # Starts the game of coin flip
        if int(bet) > 0:
            print("________________")
            print("Flipping coin...")
            flip = random.randint(1, 2)
            heads = "heads"
            tails = "tails"
            Heads = "Heads"
            Tails = "Tails"
            win_amount = bet ** 2
            lose_amount = money - bet
            total_money_win = win_amount + money
            total_money_lose = lose_amount - money
            if flip == 1:
                print("The coin landed on HEADS")
            else:
                print("The coin landed on TAILS")
            if (flip == 1 and heads == guess) or (flip == 1 and Heads == guess):
                print("_________________________")
                print("WINNER " + "£" + str(win_amount))
                print("Your new total is " + "£" + str(total_money_win))
                new_money_value = total_money_win
                return new_money_value
            if (flip == 2 and tails == guess) or (flip == 2 and Tails == guess):
                print("WINNER " + "£" + str(win_amount))
                print("Your new total is " + "£" + str(total_money_win))
                new_money_value = total_money_win
                return new_money_value
            elif (
                (flip == 1 and heads != guess)
                or (flip == 1 and Heads != guess)
                or (flip == 2 and tails != guess)
                or (flip == 2 and Tails != guess)
            ):  # if coin is 1(heads) but guess is not heads the print statement is ran
                print(
                    "YOU LOSE £" + str(bet) + " Total remaining money: £" + str(lose_amount)
                )
                new_money_value = lose_amount
                return new_money_value
        return new_money_value
        play_again()
money = 100
while (money >= 100):
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
            break
        except ValueError:
                print("Enter a number between 1 - 100")
                continue
    new_money = coin_flip(money)
    print("Remaining money = £" + str(new_money))

