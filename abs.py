boy_name = str(input("Enter boy Name:"))
girl_name = str(input("Enter girl Name:"))

boy_age = int(input("Enter boy Age:"))
girl_age = int(input("Enter girl Age:"))

print("Every boys names:" + boy_name)
print("Every girl names:" + girl_name)

age_diff = abs(boy_age-girl_age)

print("Age difference is: " + str(age_diff))