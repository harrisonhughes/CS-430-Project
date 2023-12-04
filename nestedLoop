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
