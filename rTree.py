# CS 430 Project
# Teddy Bielecki, Ethan Hinni, Harrison Hughes, Phillip Lechenauer, Ian McIntyre
# Nearest neighbor algorithm without R Tree storage to calculate the skyline of a 2D dataset

import numpy as np
import math as math
import sys as sys

def rTree(dataSet):
    """
    Calculate the skyline of a dataset using an "R Tree" and the nearest neighbor method

    @param dataSet: full dataset of value pairs in shich we will find the skyline
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    tree: holds "coordinate pairs" and uses nearest neighbor/ discard methods to iteratively solve the skyline
    @return: list of value pairs that corresponds to a perfect skyline of the data set

    """
    skyline = []
    tree = []
    maxMiles = 0 # Holds max X value in dataset
    maxPrice = 0 # Holds max Y value in dataset

    # Fill tree with "coordinates" from dataset
    for i in range(len(dataSet)):
        tree.append(dataSet[i])
        maxMiles = max(maxMiles, dataSet[i][0])
        maxPrice = max(maxPrice, dataSet[i][1])

    # 'Waiting' queue holds coordinates describing a rectangular area
    waiting = [(0, 0, maxMiles, maxPrice)]

    # Create Skyline; continue partitioning until no elements remain in the tree
    while len(waiting) > 0:
        # Pop coordinates of current region, find the nearest neighbor to bottom left of the current region
        leftOrig, bottomOrig, rightOrig, topOrig = waiting.pop(0) 
        newNode = nearestNeighbor(leftOrig, bottomOrig, rightOrig, topOrig, tree)

        # If the region contains a nearest neighbor, add it to the skyline, branch to new regions, and discard dominated values from tree
        if newNode != ():
            skyline.append(newNode)
            waiting.append((leftOrig, newNode[1], newNode[0], maxPrice)) # Create new region above newest element
            waiting.append((newNode[0], bottomOrig, maxMiles, newNode[1])) # Create new region to left of newest element
            discard(newNode, tree) # Remove all elements in tree dominated by the newest element (and remove newest element)
    return skyline

def nearestNeighbor(leftBound, bottomBound, rightBound, topBound, tree):
    """
    Find the nearest neighbor to the bottom left of the region passed

    @param leftBound: Leftmost bound of the current region of search
    @param bottomBound: Lower bound of the current region of search
    @param rightBound: Rightmost bound of the current region of search
    @param topBound: Upper bound of the current region of search
    @param tree: "Tree" of coordinates from dataset that could possibly be in the skyline
    @return nearest: coordinate pair that is within the region of search, and closest to the origin
    """
    # Keep track of nearest element and smallest distance to origin
    nearest = ()
    dist = sys.maxsize

    # Loop tgrough remaining elements in tree, ensure it is within the region, and check if it is the nearest neighbor
    for i in range(len(tree)):
        # Check if current coordinates are within region
        if(tree[i][0] >= leftBound and tree[i][0] <= rightBound and tree[i][1] >= bottomBound and tree[i][1] <= topBound):

            # Calculate distance from origin; if shortest so far, update new distance and nearest neighbor
            newDist = math.sqrt(math.pow(abs(tree[i][0] - leftBound), 2) + math.pow(abs(tree[i][1] - bottomBound), 2))
            if dist > newDist:
                dist = newDist
                nearest = tree[i]
    return nearest

def discard(origin, tree):
    """
````Discard all elements from the "tree" if they are dominated, or the element just added to the skyline

    @param origin: Tuple of the coordinates that has just been added to the skyline
    @return: none
    """
    # Loop through entire tree; if dominated, remove
    i = 0
    while i < len(tree):
        # Remove dominated elements and element that has just been added to skyline
        if tree[i][0] >= origin[0] and tree[i][1] >= origin[1]:
            del(tree[i])
        else:
            i = i + 1
    return
            
                                
                           
        
