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
    miles = np.round(miles, 2)
    price = np.round(price, 2)
    return list(zip(miles, price)) # Modify list so that each index corresponds to a (mileage, price) value pair
    
def time_algorithm(algorithm, dataSet):
    """
    Times the algorithm passed in as a parameter

    @param algorithm: algorithm to be timed
    @param dataSet: full dataset of value pairs in which we will find the skyline
    @return: time taken to run the algorithm
    """
    import time
    start = time.time()
    algorithm(dataSet)
    end = time.time()
    return end - start


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




