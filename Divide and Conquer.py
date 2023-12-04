import numpy as np
#Divide and conquer approach

def sortByMiles(dataSet):
    """
    Function to sort the data so that a median can be found
    Without this, a median cannot be found and, therefore, it can not be partitioned properly
    This will, however, increase time complexity
    @param dataSet: the data set to sort
    
    @return: a sorted dataset
    """
    if len(dataSet) <= 1:
        return dataSet
    dataSet.sort(key = lambda x: x[0])
    return dataSet

def sortByPrice(dataSet):
    """
    This function will sort by miles to allow for a median to be taken for use in the merge function
    @param dataSet: the data to sort
    @return: a dataset sorted by miles (the second parameter)
    """
    if len(dataSet) <= 1:
        return dataSet
    dataSet.sort(key = lambda x: x[1])
    return dataSet


def merge(left, right):
    """
    This function will take the two current skylines and recombine them only using those needed.
    @param left: the left partition; right: the right partition
    @return the merged skyline as things stand
    """
    #sort the partitions by the other dimension
    sortedLeft = []
    sortedRight = []
    sortedLeft = sortByPrice(left)
    sortedRight = sortByPrice(right)
    #find their medians
    leftMed = (len(left)//2) + (len(left)%2)
    rightMed = (len(right)//2) + (len(right)%2)
    #create the result list and the partitions needed from the current partitions
    result = []

    S11 = sortedLeft[:leftMed]
    S12 = sortedLeft[leftMed:]
    S21 = sortedRight[:rightMed]
    #S22 is unecessary, as it is always dominated
    result.extend(S11)

    # now remove any that are dominated by S11 in S21 and S12
    for car in S21:
        worse = False
        for other in S11:
            if car[1] > other[1] and car[0] > other[0]:
                worse = True
                break
        if not worse:
            result.append(car)

    for car in S12:
        worse = False
        for other in S11:
            if car[1] > other[1] and car[0] > other[0]:
                worse = True
                break
        if not worse:
            result.append(car)
    return result


def divAndConq(dataSet, left, right):
    """
    Divide and conquer approach to the skyline problem
    @param dataSet: the entire database to sort through and find the skyline from

    @return: the values in the skyline (those that are not dominated by any other value)
    """
    if left >= right:
        return dataSet[right:right+1]
    med = (left+right)//2 

    leftSky = divAndConq(dataSet, left, med)
    rightSky = divAndConq(dataSet, med + 1, right)
    return merge(leftSky, rightSky)
