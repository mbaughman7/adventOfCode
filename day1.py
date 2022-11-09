## PART 1
# with open("day1.txt") as myFile:
#     raw_array = myFile.readlines()
# input_array = []
# for item in raw_array:
#     item = int(item)
#     input_array.append(item)
# i = 1
# counter = 0
# for item in input_array[1::]:
#     previous = input_array[i-1]
#     i += 1
#     if item > previous:
#         counter += 1
#         print(f"{item}...{previous}")
#
# print(counter)


# PART 2
with open("day1.txt") as myFile:
    raw_array = myFile.readlines()
input_array = []
for item in raw_array:
    item = int(item)
    input_array.append(item)

triplet_list = []

i = 0
for item in input_array:
    try:
        triplet_list.append(input_array[i] + input_array[i+1] + input_array[i+2])
        i += 1
    except:
        print("all out of numbers for triplet list")
        break
j = 1
counter = 0
for item in triplet_list[1::]:
    previous = triplet_list[j-1]
    j += 1
    if item > previous:
        counter += 1
print(counter)
