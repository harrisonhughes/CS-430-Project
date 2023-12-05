# CS 430 Project
# Teddy Bielecki, Ethan Hinni, Harrison Hughes, Phillip Lechenauer, Ian McIntyre
# engine for algorithm testing

import numpy as np
import matplotlib.pyplot as plt
from nestedLoop import nestedLoop
from blockNestedLoop import block_nested_loop
from divideAndConquer import divAndConq
from mWayPartitioning import mWayPartitioning
from bTree import bTree
from rTree import rTree

def createTestData(numValues):
    """
    Creates a set of test values for two factors, both over a normal distribution
    
    @param numValues: User specified number of values to generate for a dataset
    miles: normal distribution corresponding to the mileage of a specific car (mean=80,000, sigma=20,000, size=specified parameter)
    price: normal distribution corresponding to the price of a specific car (mean=20,000, sigma=5,000, size=specified parameter)
    @return: array containing value pairs from the normal distributions from above. Any index corresponds to a value pair for a specific
        car, where the first value is the mileage, and the second value corresponds to the price
    """
    miles = np.random.normal(loc=80000, scale=20000, size=numValues)
    price = np.random.normal(loc=20000, scale=5000, size=numValues)
    price -= .055 * miles # Making price inversely proportional to miles
    price = np.maximum(price, 500)
    
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
    if algorithm == divAndConq:
        algorithm(dataSet, 0, len(dataSet) - 1)
    else:
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
    # 10 Trials over 10 different data sizes
    numTrials = 10
    numSizes = 10
    dataSize = [] # List to hold all tested data sizes

    # Smaller test for all 6 algorithms
    """
    # Initialize variables for time trials
    nest, bnest, dc, mw, bt, rt = 0, 0, 0, 0, 0, 0 # Time of a single run
    nested, blocknested, divconq, mway, btree, rtree = [], [], [], [], [], [] # Average time at a certain data size

    # Execute time trials
    for i in range(numSizes):
        size = (i + 1) * 10000 # !0,000 increments between trials, starting at 10,000

        # Find total time for each algorithm to complete "numTrials" number of executions
        for j in range(numTrials):
            nums = createTestData(size)

            # Summation of execution time for all trials 
            nest += time_algorithm(nestedLoop, nums)
            bnest += time_algorithm(block_nested_loop, nums)
            dc += time_algorithm(divAndConq, nums)
            mw += time_algorithm(mWayPartitioning, nums)
            bt += time_algorithm(bTree, nums)
            rt += time_algorithm(rTree, nums)

        # Append average time to execute, divide by numTrials
        nested.append(nest / numTrials)
        blocknested.append(bnest / numTrials)
        divconq.append(dc / numTrials)
        mway.append(mw / numTrials)
        btree.append(bt / numTrials)
        rtree.append(rt / numTrials)

        # Record current data size, reset summation variables
        dataSize.append(size)
        nest, bnest, dc, mw, bt, rt = 0, 0, 0, 0, 0, 0

    plt.figure(figsize=(10, 6))
    plt.plot(dataSize, nested, label="Nested Loop (SQL)")
    plt.plot(dataSize, blocknested, label="Block Nested Loop")
    plt.plot(dataSize, divconq, label="Divide and Conquer")
    plt.plot(dataSize, mway, label="M-Way Partitioning")
    plt.plot(dataSize, btree, label="B Tree")
    plt.plot(dataSize, rtree, label="R Tree")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution time (seconds)")
    plt.title("Comparison of different algorithms")
    plt.legend()
    plt.show()
    """
        
    # Larger test for faster algorithms (no R Tree or Nested Loop)
    
    # Initialize variables for time trials
    bnest, dc, mw, bt = 0, 0, 0, 0 # Time of a single run
    blocknested, divconq, mway, btree = [], [], [], [] # Average time at a certain data size

    # Execute time trials
    for i in range(numSizes):
        size = (i + 1) * 100000 # 100,000 increments between trials, starting at 100,000
        
        # Find total time for each algorithm to complete "numTrials - 1" number of executions
        for j in range(numTrials):
            nums = createTestData(size)

            # Summation of execution time for all trials 
            bnest += time_algorithm(block_nested_loop, nums)
            dc += time_algorithm(divAndConq, nums)
            mw += time_algorithm(mWayPartitioning, nums)
            bt += time_algorithm(bTree, nums)

        # Append average time to execute, divide by numTrials
        blocknested.append(bnest / numTrials)
        divconq.append(dc / numTrials)
        mway.append(mw / numTrials)
        btree.append(bt / numTrials)

        # Record current data size, reset summation variables
        dataSize.append(size)
        nest, bnest, dc, mw, bt, rt = 0, 0, 0, 0, 0, 0

    #Plot Data
    plt.figure(figsize=(10, 6))
    plt.plot(dataSize, blocknested, label="Block Nested Loop")
    plt.plot(dataSize, divconq, label="Divide and Conquer")
    plt.plot(dataSize, mway, label="M-Way Partitioning")
    plt.plot(dataSize, btree, label="B Tree")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution time (seconds)")
    plt.title("Comparison of different algorithms")
    plt.legend()
    plt.show()
        
   
