# CS 430 Project
# Teddy Bielecki, Ethan Hinni, Harrison Hughes, Phillip Lechenauer, Ian McIntyre
# Binary Tree algorithm to find the skyline of a dataset

from nestedLoop import nestedLoop

def bTree(dataSet):
    """
    Binary Tree strategy of finding the skyline. Starts by sorting each car's miles and price. Then finds the earliest car in
    both the sorted miles array and sorted price array. Delete all cars below that earliest common car. Perform another
    algorithm on the rest of the data
    
    @param dataSet: full dataset of value pairs in shich we will find the skyline
    skyline: holds the full data set and loops through, removing any value pair that is dominated by another
    @return: list of value pairs that corresponds to a skyline of the data set using bTree
    """
    skyline = dataSet.copy()

    # get two separate tuple lists
    miles, price = zip(*skyline)

    milesDict = {}
    priceDict = {}
    index = 0

    # making each dictionary have a key of the car number and value of miles / price
    while (index < len(skyline)):
        milesDict[index] = miles[index]
        priceDict[index] = price[index]
        index = index + 1
    
    # sort price and miles dictionary from lowest to highest miles / price
    sortedMiles = dict(sorted(milesDict.items(), key=lambda item: item[1]))
    sortedPrice = dict(sorted(priceDict.items(), key=lambda item: item[1]))

    # trace through each dictionary from the beginning until we have a common car
    # this common car is part of the skyline
    # the "key" is the number of the car
    milesKeys = list(sortedMiles.keys())
    priceKeys = list(sortedPrice.keys())

    prevMiles = [] # values of miles that we have seen since the beginning of the sorted list
    prevPrice = [] # values of prices that we have seen since the beginning of the sorted list
    index = 0
    milesIndex = -1 # index of where the cutoff will be for miles when common car is found
    priceIndex = -1 # index of where the cutoff will be for price when common car is found
    commonValueFound = False

    # trace through each dictionary from the beginning until we have a common car
    # this common car is part of the skyline
    while (not commonValueFound):
        if (milesKeys[index] in prevPrice or milesKeys[index] == priceKeys[index]):
            # the number of the car that will be the cutoff for what makes the skyline
            commonValueFound = True
            milesIndex = index
            priceIndex = priceKeys.index(milesKeys[index])
        elif (priceKeys[index] in prevMiles):
            commonValueFound = True
            priceIndex = index
            milesIndex = milesKeys.index(priceKeys[index])
        else:
            # common car not found. Store car number
            prevMiles.append(milesKeys[index])
            prevPrice.append(priceKeys[index])
        index = index + 1

    # delete every car from the skyline that is below the common car in each dictionary
    startIndex = len(milesKeys) - 1 # we will start at the end of each array
    endIndex = milesIndex if milesIndex < priceIndex else priceIndex
    while (startIndex > endIndex):
        if (startIndex > milesIndex):
            del milesKeys[startIndex]
        if (startIndex > priceIndex):
            del priceKeys[startIndex]
        startIndex = startIndex - 1
    

    # put arrays back together for the possible skyline keys
    possibleSkylineKeys = milesKeys + priceKeys

    # add (miles, price) tuples to the current skyline
    currentSkyline = []
    for key in possibleSkylineKeys:
        currentSkyline.append(tuple((milesDict[key], priceDict[key])))

    # perform an algorithm on the rest of the cars that were before the common car since they
    # may or may not be in the skyline. Make that result the final skyline
    skyline = nestedLoop(currentSkyline)
    
    return skyline 
