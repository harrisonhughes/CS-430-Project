# CS 430 Project
# Harrison Hughes
# R Tree nearest neighbor algorithm to calculate the skyline of a 2D dataset, using rTree Python extension

import numpy as np
from rtree import index 

def rTree(dataSet):
    """
    Calculate the skyline of a dataset using an R Tree and the nearest neighbor method, using rTree Python extension

    @param dataSet: full dataset of value pairs in shich we will find the skyline
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a perfect skyline of the data set

    """
    skyline = []

    # Create tree and fill with every element from dataSet
    tree = index.Index()
    for i in range(len(dataSet)):
        tree.insert(i, (*dataSet[i], *dataSet[i])) # insert(index, (left, bottom, right, top coordinates))

    # Maximum values of the factors
    maxMiles = tree.bounds[2] 
    maxPrice = tree.bounds[3]

    # 'Waiting' queue holds coordinates describing a rectangular area
    waiting = [(0, 0, maxMiles, maxPrice)] 

    # Create Skyline; continue partitioning until no elements remain in the tree
    while len(waiting) > 0:
        leftOrig, bottomOrig, rightOrig, topOrig = waiting.pop(0) # Coordinates of the current area in which we are searching
        region = list(tree.intersection((leftOrig, bottomOrig, rightOrig, topOrig))) # List of tree element indices within the current area

        # If the current area is not empty, find the skyline element within 
        if len(region) > 0:
            
            # Brute force way to ensure that the nearest neighboring point is within the same region
            closestPoints = list(tree.nearest((leftOrig, bottomOrig, leftOrig, bottomOrig), tree.count((0, 0, maxMiles, maxPrice))))
            for i in closestPoints:
                if i in region:
                    newIndex = i
                    break

            # Add nearest neighbor to skyline, and remove from tree
            skyline.append(dataSet[newIndex])
            tree.delete(newIndex, (*dataSet[newIndex], *dataSet[newIndex]))

            # Remove all tree elements that are guaranteed to be dominated by the new skyline element
            discardRegion = list(tree.intersection((*dataSet[newIndex], maxMiles, maxPrice)))
            for i in discardRegion:
                tree.delete(i, (*dataSet[i], *dataSet[i]))

        # If the region had multiple elements, partition further (add new origin coordinates to the waiting queue)
        if len(region) > 1:
            waiting.append((0, dataSet[newIndex][1], dataSet[newIndex][0], maxPrice)) # Create new region above
            waiting.append((dataSet[newIndex][0], 0, maxMiles, dataSet[newIndex][1])) # Create new region to the left
            
    return skyline
