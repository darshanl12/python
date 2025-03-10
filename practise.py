#pizza --->large (300)
#pizza --->small (200
#pizza ------> regular (100)

# add extra  cheese (10)
#use cash on delivery ---10 % discout
#use debit card -------50 % discout

print("Welcome to Dominos")
menu = input("Do you want to order pizza? (yes/no): ")
if menu.lower() == "yes" or "y":
    print("Thanks for your choice")
    size = input("Select your pizza size! (small/larger/regular): ")
    if size.lower() == "small" or "s":
        price = 200
        print(f"Your bill is: {price}")
    elif size.lower() == "larger" or "l":
        price = 300
        print(f"Your bill is: {price}")
    elif size.lower() == "regular" or "r":
        price = 100
        print(f"Your bill is: {price}")
    cheese = input("Do you want extra cheese? (yes/no): ")
    if cheese.lower() == "yes" or "y":
        add = 10
        print(f"Successfully added extra cheese: {add}")
        total = price + add
        print(f"Your total bill is: {total}")
    else:
        print("No extra cheese")
else:
    print("Please come back again")
    
