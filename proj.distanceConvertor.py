# logic of project
# killometer to miles----> ex. 10 killo  to 6.2137miles  ( #logic is divided killo by 1.609 )
#  miles to killometer----> ex. 20 miles to  32.169 killo ( #logic is multiplied miles by 1.609 )


distance = int(input("enter the distanc travelled :"))
unit = input("input type is  K for kms or M for miles :")

if unit.upper() == "K":     #upper means  it will convert all the input to upper case

    converted = distance/1.609
    print(f"you have covered {converted} miles")

elif unit.upper() == "M":    #upper  means  it will convert all the input to upper case
    coverted = distance * 1.609
    print(f"you have covered {coverted} killo")

else:
    print("wrong input")

