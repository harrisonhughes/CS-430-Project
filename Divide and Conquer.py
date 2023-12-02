#This part was taken from the main project
import numpy as np

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

#Divide and conquer approach

def sortByMiles(dataSet):
    """
    Function to sort the data so that a median can be found
    Without this, a median cannot be found and, therefore, it can not be partitioned properly
    This will, however, increase time complexity
    @param dataSet: the data set to sort
    
    @return: a sorted dataset
    """
    dataSet.sort()
    return dataSet

def sortByPrice(dataSet):
    """
    This function will sort by miles to allow for a median to be taken for use in the merge function
    @param dataSet: the data to sort
    @return: a dataset sorted by miles (the second parameter)
    """
    end = len(dataSet)-1
    for i in range(0, end):
        for j in range(0, end-i):
            if dataSet[j][1] < dataSet[i][1]:
                temp = dataSet[i]
                dataSet[i] = dataSet[j]
                dataSet[j] = temp
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
    S11 = []
    S12 = []
    S21 = []
    S11 = sortedLeft[:leftMed]
    S12 = sortedLeft[leftMed:]
    S21 = sortedRight[:rightMed]
    #S22 is unecessary, as it is always dominated
    #S11 will always be necessary, as they are always better
    result.append(S11)
    #now remove any that are dominated by S11 in S21 and S12
    i = 0
    miniMaxPrice = S11[0][1]
    miniMaxMiles = S11[0][0]
    for i in range(len(S11)):
        if S11[i][0] < miniMaxMiles:
            miniMaxMiles = S11[i][0]
    for i in range(len(S21)):
        if S21[i][1] < miniMaxPrice:
            result.append(S21[i])

    for i in range(len(S12)):
        if S12[i][0] < miniMaxPrice:
            result.append(S12[i])

    return result


def divAndConq(dataSet, left, right):
    """
    Divide and conquer approach to the skyline problem
    @param dataSet: the entire database to sort through and find the skyline from

    @return: the values in the skyline (those that are not dominated by any other value)
    """
    skyline = []
    if left >= right:
        skyline.append(dataSet[right])
        return skyline
    med = (left-right)//2 

    leftSet = dataSet[:med]
    rightSet = dataSet[med:]
    leftSky = divAndConq(leftSet, 0, len(leftSet)-1)
    rightSky = divAndConq(rightSet, 0, len(rightSet)-1)
    skyline = merge(leftSky, rightSky)
    return skyline

if __name__=="__main__":
    dataSet = createTestData(100)
    sortByMiles(dataSet)
    skyline = divAndConq(dataSet, 0, len(dataSet)-1)
    print(skyline)
