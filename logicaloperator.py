# #And 
# #this print only by all canditions are true

known_python =  True
degree = True

if known_python and degree:
    print("you are shortlist")

# #OR
# #its print   if any of one conditions are true its give output other condioton is have false

known_python = True
degree = False
skills = False

if known_python or degree or skills:
    print("you are shortlist")


#NOT
#TRUEE EDARE FALSE ANTA
#FALSE EDDARE TRUEE ANTA
# NOT edu erabaradu yendu helatte

#ex.1
known_python = True
degree = False
#NOT operator is used to reverse the boolean value
if not known_python:
    print("you are shortlist") # error because  known_python is true so it will not print this line

#ex.2

known_python = False
degree = False
#NOT operator is used to reverse the boolean value
if not known_python:
    print("you are shortlist") # it will print this line because known_python is false so



    #( if olage logical operator use madta AND & OR & NOT onde condition olage multile opertor use madbod
        # example:- if known_python and not degree  and skills:  )



