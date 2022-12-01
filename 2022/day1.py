with open("test_data.txt") as myFile:
    raw_array = myFile.readlines()

adder = 0
counter = 0
snack_dict = {}
top_three_total = 0

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
top_three_total += highest_cal

del snack_dict[highest_cal_elf]

second_highest_elf = max(snack_dict, key=snack_dict.get)
second_highest_cal = max(snack_dict.values())

top_three_total += second_highest_cal
del snack_dict[second_highest_elf]

third_highest_elf = max(snack_dict, key=snack_dict.get)
third_highest_cal = max(snack_dict.values())

top_three_total += third_highest_cal

print(top_three_total)

