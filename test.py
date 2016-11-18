def stdDevOfLengths(L):
    """
        L: a list of strings
        
        returns: float, the standard deviation of the lengths of the strings,
        or NaN if L is empty.
        """
    if L ==[]:
        return float('NaN')
    else:
        sum = 0
        for i in L:
            sum += float(i)
        mean = sum/len(L)
        num = 0
        for i in L:
            num += (float(i)-mean)**2
        segma = (num/len(L))**(0.5)
        coeff = segma/mean
        return segma, coeff

print (stdDevOfLengths([10, 4, 12, 15, 20, 5]))
