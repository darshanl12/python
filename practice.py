value= int(input("Enter a id: "))
letter = "B"

if value<= 100:
    print("Correct code")

elif value >=100:
    print("Incorrect code")


else:
    print("doesnt match")

if letter  == "A":

   print("yes this is A") 

else:
    print("no this is not A")

print("final id result is:"+  str(value))
submit =  input("Do you want to submit the id? (yes/no): ")
if submit  == "yes":
    print("id submitted")
elif submit  == "no":
    print("id not submitted")

print('thank you')



# result = True
# if result:
#     print("passed")

# else:
#     print("failed")