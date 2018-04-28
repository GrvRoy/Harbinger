import sys
import math


def main():
    input_from_file()


# This method returns the value after using the sigmoid activation.
def sigmoid(x, derivative):
    if not derivative:
        return 1/(1 + math.exp(-x))
    else:
        return x * (1 - x)

#This method returns the normalised values of the maximum and minimum temperatures.
def normalisation(x):
    
    x_max = float(max(x))
    x_min = float(min(x))
    n = len(x)
    x_n = []
    for i in range(0,n):
       x_n.append((float(x[i]) - float(x_min)) /(float(x_max) - float(x_min)))

    return x_n

    
# This method inputs data from file into lists
def input_from_file():
    file_to_open = "book1.txt"
    f = open(file_to_open, "r")
    lines = f.readlines()
    min_temp = []
    max_temp = []
    # x.split()[1] refers to data in second column
    for x in lines:
        max_temp.append(float(x.split('\t')[2]))
        min_temp.append(x.split('\t')[3].replace("\n", ""))
    f.close()
    first_10_values_min = min_temp[1:11]
    first_10_values_max = max_temp[1:11]
    n_max = []
    n_min = []
    n_max = normalisation(first_10_values_max)
    n_min = normalisation(first_10_values_min)
    print(n_max)
    print(n_min)
    #print(first_10_values_min)
    #print(first_10_values_max)


if __name__ == "__main__":
    sys.exit(main())
