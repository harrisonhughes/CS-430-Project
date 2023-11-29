# CS 430 Project
# Harrison Hughes
# engine for algorithm testing

import numpy as np
import matplotlib.pyplot as plt

def createTestData(numValues):
    """
    Creates a set of test values for two factors, both over a normal distribution
    
    @param numValues: User specified number of values to generate for a dataset
    miles: normal distribution corresponding to the mileage of a specific car (mean=80,000, sigma=20,000, size=specified parameter)
    price: normal distribution corresponding to the price of a specific car (mean=20,000, sigma=5,000, size=specified parameter)
    @return: array containing value pairs from the normal distributions from above. Any index corresponds to a value pair for a specific
        car, where the first value is the mileage, and the second value corresponds to the price
    """
    np.random.seed(0)
    miles = np.random.normal(loc=80000, scale=20000, size=numValues)
    price = np.random.normal(loc=20000, scale=5000, size=numValues)
    for i in range(numValues): # Truncate values to 2 decimal points
        miles[i] = round(miles[i], 2)
        price[i] = round(price[i], 2)
    return list(zip(miles, price)) # Modify list so that each index corresponds to a (mileage, price) value pair

def nestedLoop(dataSet):
    """
    Brute force nested loop strategy to find the skyline
    
    @param dataSet: full dataset of value pairs in shich we will find the skyline
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a perfect skyline of the data set
    """
    skyline = dataSet.copy()
    i = 0
    while i < len(skyline):
        dominated = False
        j = i + 1
        while j < len(skyline):
            if skyline[i][0] <= skyline[j][0] and skyline[i][1] <= skyline[j][1]: # Car with inner loop index (j) is dominated, no need to increment
                del skyline[j]
            elif skyline[i][0] >= skyline[j][0] and skyline[i][1] >= skyline[j][1]: # Car with outer loop index (i) is dominated, remove and break loop
                del skyline[i]
                dominated = True # Remember not to increment outer index, as we have deleted the current value
                break
            else: # Else, neither of the cars dominated one another, so move on to the next one
                j = j + 1
        if(dominated == False):
            i = i + 1 # Car from outer loop index was not dominated, so keep it in the set and increment to the next
    return skyline


def plot_data(nums, skyline, title = "Skyline of Car Mileage vs. Price"):
    """
    Plots the data from the dataset and the skyline

    @param title: title of the plot
    @param nums: full dataset of value pairs in which we will find the skyline
    @param skyline: list of value pairs that corresponds to a perfect skyline of the data set
    @return: none
    """
    plt.scatter(*zip(*nums))  # Create scatterplot
    plt.scatter(*zip(*skyline))
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    nums = createTestData(100)
    skyline = nestedLoop(nums)
    plot_data(nums, skyline)




