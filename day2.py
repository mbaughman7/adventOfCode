with open("day2.txt") as myFile:
    raw_array = myFile.readlines()

depth = 0
distance = 0
aim = 0

for item in raw_array:
    shortlist = item.split()
    if shortlist[0] == 'forward':
        distance += int(shortlist[1])
        depth += (aim * int(shortlist[1]))
    elif shortlist[0] == 'down':
        aim += int(shortlist[1])
    else:
        aim -= int(shortlist[1])

print(depth*distance)