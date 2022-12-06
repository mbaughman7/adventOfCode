with open("day2_data.txt") as myFile:  #change this to be done automatically
    raw_array = myFile.readlines()

potential_rounds = {('A','X'):4,('A','Y'):8,('A','Z'):3,('B','X'):1,('B','Y'):5,('B','Z'):9,('C','X'):7,('C','Y'):2,('C','Z'):6}

recalculated_rounds = {('A','X'):3,('A','Y'):4,('A','Z'):8,('B','X'):1,('B','Y'):5,('B','Z'):9,('C','X'):2,('C','Y'):6,('C','Z'):7}

total = 0

for line in raw_array:
    temp_tuple = (line[0],line[2])
    if temp_tuple in recalculated_rounds:
        total += recalculated_rounds[temp_tuple]

print(total)


