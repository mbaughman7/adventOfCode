with open("test_data.txt") as myFile:  #change this to be done automatically
    raw_array = myFile.readlines()

adder = 0
counter = 0
snack_dict = {}

for item in raw_array:
    if(item != '\n'):
        adder += int(item)
    else:
        counter += 1
        snack_dict[counter] = adder
        adder = 0

# catch the last one:
counter += 1
snack_dict[counter] = adder

highest_cal_elf = max(snack_dict, key=snack_dict.get)
highest_cal = max(snack_dict.values())

print(highest_cal_elf)
print(snack_dict)
print(highest_cal)
#########################
# for part 2, add the top calorie count to top_three_total, delete it from the dict,
# then find next highest, add it, delete it from dict, and so on.
def addTopSpots(num):
    top_three_total = 0
    for i in range(num):
        highest_elf = max(snack_dict, key=snack_dict.get)
        high_cal = max(snack_dict.values())
        top_three_total += high_cal
        del snack_dict[highest_elf]
    print(top_three_total)

addTopSpots(3)

