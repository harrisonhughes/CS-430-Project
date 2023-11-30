# 430 final project
# Teddy Bielecki
# m-way partitioning algorithm

import numpy as np
import matplotlib.pyplot as plt
import sys
import math
import algorithmEngine

def mWayPartitioning(dataSet):
    """
    Partitioning strategy to find the skyline
    
    @param dataSet: full dataset of value pairs in which we will find the skyline
    partitions: holds the full data set and splits it into m partitions
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a perfect skyline of the data set
    """
    available_memory = sys.getsizeof(dataSet)
    m = math.ceil(len(dataSet) * .0075)
    while(m > available_memory):
        m = math.floor(m * .9)
    
    potentialSkyLines = []
    partitions = []
    skyline = dataSet.copy()
    for i in range(m):
        partitions.append([])
    for i in range(len(skyline)):
        partitions[i % m].append(skyline[i])
    for i in range(m):
        potentialSkyLines.extend(nestedLoop(partitions[i]))
        
    potentialSkyLines = mergeSkylines(potentialSkyLines)
    return potentialSkyLines

def nestedLoop(partition):
    """
    Brute force nested loop strategy to find the skyline of the given partition
    
    @param dataSet: partitioned dataset of value pairs in which we will find the skyline
    skyline: holds the all the values in this data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a perfect skyline of the data set
    """
    skyline = partition.copy()
    i = 0
    while i < len(skyline):
        dominated = False
        j = i + 1
        while j < len(skyline):
            if dominates(skyline[i], skyline[j]): # Car with inner loop index (j) is dominated, no need to increment
                del skyline[j]
            elif dominates(skyline[j], skyline[i]): # Car with outer loop index (i) is dominated, remove and break loop
                del skyline[i]
                dominated = True # Remember not to increment outer index, as we have deleted the current value
                break
            else: # Else, neither of the cars dominated one another, so move on to the next one
                j = j + 1 
        if(dominated == False):
            i = i + 1 # Car from outer loop index was not dominated, so keep it in the set and increment to the next
    return skyline

def mergeSkylines(potentialSkyLines):
    """
    Merges the skylines from each partition into a single skyline
    
    @param potentialSkyLines: list of skylines from each partition
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a perfect skyline of the data set
    """
    result = []
    i = 0
    while i < len(potentialSkyLines):
        dominated = False
        j = i + 1
        while j < len(potentialSkyLines):
            if dominates(potentialSkyLines[i], potentialSkyLines[j]): # Car with inner loop index (j) is dominated, no need to increment
                del potentialSkyLines[j]
            elif dominates(potentialSkyLines[j], potentialSkyLines[i]): # Car with outer loop index (i) is dominated, remove and break loop
                del potentialSkyLines[i]
                dominated = True # Remember not to increment outer index, as we have deleted the current value
                break
            else: # Else, neither of the cars dominated one another, so move on to the next one
                j = j + 1 
        if(dominated == False):
            result.append(potentialSkyLines[i])
            i = i + 1 # Car from outer loop index was not dominated, so keep it in the set and increment to the next
    return result

def dominates(car1, car2):
    """
    Determines if car1 dominates car2
    
    @param car1: first car to compare
    @param car2: second car to compare
    @return: True if car1 dominates car2, False otherwise
    """
    if car1[0] <= car2[0] and car1[1] <= car2[1]:
        return True
    elif car1[0] >= car2[0] and car1[1] >= car2[1]:
        return False
    else:
        return False

data = algorithmEngine.createTestData(1000)
skyline = mWayPartitioning(data)
algorithmEngine.plot_data(data, skyline, "M-Way Partitioning Algorithm")