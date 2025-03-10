#1.    print list
heroes = ['puneeth', " yash " , "rajkumar"]
print(heroes)

#2   .    print list with index print particular item in list

heroes = ['puneeth', " yash " , "rajkumar"]
           #0          #1         #2
print(heroes[0])  # prints: puneeth

#3.   replace  particular item in list

heroes = ['puneeth', " yash " , "rajkumar"]
heroes[0] = 'darshan'   
print(heroes)  # prints: 'darshan', ' yash ', 'rajkumar

#4. add the item in existing list

heroes = ['puneeth', " yash " , "rajkumar"]

heroes.append("darshan")
print(heroes)      # prints: ['puneeth', ' yash ', 'rajkumar', 'darshan


# 5..insert the item in existiong list,  insert at particular index position 

heroes = ['puneeth', " yash " , "rajkumar"]
          #0            #1       #2  
heroes.insert(2,"shankarnag")
print(heroes)  # prints: 'puneeth', ' yash ', 'shankarnag" rajkumar'

#6 . remove the item from list

heroes = ['puneeth', " yash " , "rajkumar"]

heroes.remove("rajkumar")
print(heroes)  # prints: 'puneeth', ' yash '

#7.clear all the item in list

heroes = ['puneeth', " yash " , "rajkumar"]

heroes.clear()
print(heroes)  # prints: []

# pop this is remove last item in the list

heroes = ['puneeth', " yash " , "rajkumar"]
heroes.pop()    
print(heroes)

# 8. sort the list in ascending order

heroes = ['puneeth', " yash " , "rajkumar"]
heroes.sort()
print(heroes)  # prints: ['puneeth', ' yash ', 'rajk

#  9. sort the list in descending order
heroes = ['puneeth', " yash " , "rajkumar"]

heroes.sort(reverse=True)
print(heroes)  # prints: ['yash', 'rajkumar', 'pune

#  10. reverse the list
heroes = ['puneeth', " yash " , "rajkumar"]
heroes.reverse()
print(heroes)  # prints: ['rajkumar', ' yash ', 'pune

#  11. count the item in list
heroes = ['puneeth', " yash " , "rajkumar"]
print(heroes.count(" yash "))# prints: 1


# 12. find the index of item in list
heroes = ['puneeth', " yash " , "rajkumar"]
print(heroes.index(" yash "))# prints: 1

# how add list in existing list

heroes = ['puneeth', " yash " , "rajkumar"]
Numbers = [ 12,23,54,87,22]
heroes.extend(Numbers)
print(heroes)








