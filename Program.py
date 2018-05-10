import sys
import math
import random
import matplotlib.pyplot as plt


def main():
    input_from_file()


# This method returns the value after using the sigmoid activation.
def sigmoid(x, derivative):
    if not derivative:
        return 1 / (1 + math.exp(-x))
    else:
        return sigmoid(x, False) * (1 - sigmoid(x, False))


def squared_error(target, output):

    error_value = 0.7 * math.pow((target - output), 2)
    error_value = 0.5 * math.pow((target - output), 2)
    return error_value


def update_weights(target, output, weights, inputs):
    for j in range(0, len(weights) - 1):
        dw = 0.7 * inputs[j] * (target - output) * output * (1 - output)
        weights[j] = weights[j] + dw
    return weights


def train(data_max, data_min, hum_max, hum_min, weights):
    output_data = []
    for i in range(0, len(data_max) - 2):
        output = sigmoid(data_max[i] * weights[0] + data_min[i] * weights[1] + hum_max[i] * weights[2] + hum_min[i] *
                         weights[3], False)
        output_data.append(output)
        target = data_max[i + 1]
        inputs = [data_max[i], data_min[i], hum_max[i], hum_min[i]]
        error = squared_error(target, output)
        print(error)
        if error > 0.0001:
            weights = update_weights(target, output, weights, inputs)

    for i in range(0, len(weights) - 1):
        dw = inputs[i] * (target - output) * output * (1 - output)
        weights[i] = weights[i] - dw
    return weights


def train(data_max, data_min, weights):
    output_data = []
    for i in range(0, len(data_max) - 2):
        output = sigmoid(data_max[i] * weights[0] + data_min[i] * weights[1], False)
        output_data.append(output)
        target = data_max[i+1]
        inputs = [data_max[i], data_min[i]]
        error = squared_error(target, output)
        print error
        if error > 0.0001:
            weights = update_weights(target, output, weights, inputs)
    return output_data


# This method returns the normalised values of the maximum and minimum temperatures.
def normalisation(x):
    x_max = float(max(x))
    x_min = float(min(x))
    n = len(x)
    x_n = []
    for i in range(0, n - 1):
    for i in range(0, n-1):

        x_n.append((float(x[i]) - float(x_min)) / (float(x_max) - float(x_min)))
    return x_n


# This method inputs data from file into lists
def input_from_file():
    file_to_open = "book1.txt"
    f = open(file_to_open, "r")
    lines = f.readlines()
    min_temp = []
    max_temp = []
    hum_max = []
    hum_min = []
    weights = []
    # x.split()[1] refers to data in second column
    for x in lines:
        hum_min.append(float(x.split('\t')[0]))
        hum_max.append(float(x.split('\t')[1]))
        max_temp.append(float(x.split('\t')[2]))
        min_temp.append(float(x.split('\t')[3].replace("\n", "")))
        
    f.close()
    first_200_values_min = min_temp[1:300]
    first_200_values_max = max_temp[1:300]
    first_200_values_h_max = hum_max[1:300]
    first_200_values_h_min = hum_min[1:300]
    normalised_max = normalisation(first_200_values_max)
    normalised_min = normalisation(first_200_values_min)
    normal_hum_max = normalisation(first_200_values_h_max)
    normal_hum_min = normalisation(first_200_values_h_min)
    weights.append(random.random())
    weights.append(random.random())
    weights.append(random.random())
    weights.append(random.random())
    output_data = train(normalised_max, normalised_min,normal_hum_max,normal_hum_min, weights)
    f.close()
    first_10_values_min = min_temp[1:11]
    first_10_values_max = max_temp[1:11]
    normalised_max = normalisation(first_10_values_max)
    normalised_min = normalisation(first_10_values_min)
    weights.append(random.random())
    weights.append(random.random())
    output_data = train(normalised_max, normalised_min, weights)
    plt.plot(normalised_max)
    plt.plot(output_data)
    plt.show()


if __name__ == "__main__":
    sys.exit(main())
