# # 2d list in matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

# #  Accessing elements in 2d list in matrix

matrix = [
    [1,2,3], # row 0 # index  0, 1, 2

    [4,5,6], # row 1  # index  0,1,2
    [7,8,9]  #row 2  # index 0,1,2
]
print(matrix[0][2]) #0--> row & 2---> index position


# # ex.1 

team = [
    ["rohit","virat","dhoni"],
    ["kl rahul","kapil",  "sachin"],
    ["boobrah","siraj","chahal"]

]

print(team)

# ex.2 replace in 2d list

team = [
    ["rohit","virat","dhoni"],
    ["kl rahul","kapil",  "sachin"],
    ["boobrah","siraj","chahal"]

]
team[1][1]="surya kumar"   #--->  1--> row & 1--> index position na replace kapil to surya 
print(team)

# ex.3 2d list in for loop

team = [
    ["rohit","virat","dhoni"],
    ["kl rahul","kapil",  "sachin"],
    ["boobrah","siraj","chahal"]

]

for particula_team in team:
    print(f"team_is:{particula_team}")
    for team_A in particula_team:
        print(team_A)
        if (team_A == "rohit"):
            print("Best Captain forever")
