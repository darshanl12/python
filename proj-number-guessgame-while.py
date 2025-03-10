# number guessing game
#gusiing number 10 edre won the game barbeku
#guess madalu 3 chance erutte
# 3 chance alli guess agillla andare lost the game barbeku 

winning_number = 10
guess_count = 0
while guess_count<3:
    guess_count = guess_count+1
    guess = int(input("enter your guessing Number:"))
    if guess == winning_number:
        print("you WON !")
        break
else:
    print("you lost the game")
    print("better luck for next time")


