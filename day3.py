from collections import Counter

with open("day3.txt") as myFile:
    raw_array = myFile.readlines()

gamma_array = []
epsilon_array = []

i=0
temp_list = []

for n in range(len(raw_array[0])-1):
    for item in raw_array:
        temp_list.append(item[i])
    c = Counter(temp_list)
    common = c.most_common()[0][0]
    least_common = c.most_common()[1][0]
    print(common)
    gamma_array.append(common)
    epsilon_array.append(least_common)
    i += 1
    temp_list.clear()

gamma = ''.join(gamma_array)
epsilon = ''.join(epsilon_array)

print(int(gamma,2) * int(epsilon,2))
