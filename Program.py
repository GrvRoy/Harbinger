file = "book1.txt"
f = open(file, "r")
lines = f.readlines()
min_temp = []
max_temp = []
# x.split()[1] refers to data in second column
for x in lines:
    max_temp.append(float(x.split('\t')[2]))
    min_temp.append(x.split('\t')[3].replace("\n", ""))
f.close()
first_10_values_min = []
first_10_values_max = []
first_10_values_min = min_temp[1:11]
first_10_values_max = max_temp[1:11]
print(first_10_values_min)
print(first_10_values_max)