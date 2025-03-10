# # for loop in numbers 
numbers = [10, 20, 30, 40]
total = 0
for values in numbers:
    total=total+values
print(total)


# #for loop in strings

names = ["darshan", "basva", "durga"]

for indiv_names in names:
    print(indiv_names)


#for loop in strings use ranges

names = ["darshan", "durga","basva","kushi"]
        # 0            1      2       3
for indiv_names in range(2,3):
    print(indiv_names)
    print(names[indiv_names])


# for loop 

names = ["darshan", "durga","basva","kushi"]
        # 0            1      2       3
for indiv_names in range(len(names)):
    print(indiv_names)
    print(names[indiv_names])


# for loop in using if condition

names = ["darshan", "durga","basva","kushi"]
        # 0            1      2       3
for indiv_names in range(len(names)):
    if (names[indiv_names]=="darshan"):
        print(f"found darshan {indiv_names}")
    