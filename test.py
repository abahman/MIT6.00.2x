#def stdDevOfLengths(L):
#    """
#        L: a list of strings
#        
#        returns: float, the standard deviation of the lengths of the strings,
#        or NaN if L is empty.
#        """
#    if L ==[]:
#        return float('NaN')
#    else:
#        sum = 0
#        for i in L:
#            sum += float(i)
#        mean = sum/len(L)
#        num = 0
#        for i in L:
#            num += (float(i)-mean)**2
#        segma = (num/len(L))**(0.5)
#        coeff = segma/mean
#        return segma, coeff
#
#print (stdDevOfLengths([10, 4, 12, 15, 20, 5]))

#import random
#
#def F():
#    mylist = []
#    r = 1
#    
#    if random.random() > 0.99:
#        r = random.randint(1, 10)
#    for i in range(r):
#        random.seed(1000)
#        if random.randint(1, 10) > 3:
#            number = random.randint(1, 10)
#            if number not in mylist:
#                mylist.append(number)
#    print(mylist)
#
#def G():
#    random.seed(10000)
#    mylist = []
#    r = 1
#    
#    if random.random() > 0.99:
#        r = random.randint(1, 10)
#    for i in range(r):
#        if random.randint(1, 10) > 3:
#            number = random.randint(1, 10)
#            mylist.append(number)
#            print(mylist)
#
#print(F())
#print(G())
#
#
#def song_playlist(songs, max_size):
#    """
#        songs: list of tuples, ('song_name', song_len, song_size)
#        max_size: float, maximum size of total songs that you can fit
#        
#        Start with the song first in the 'songs' list, then pick the next
#        song to be the one with the lowest file size not already picked, repeat
#        
#        Returns: a list of a subset of songs fitting in 'max_size' in the order
#        in which they were chosen.
#        """
#    
#    playlist = []
#    size = 0
#    
#    if songs[0][2] > max_size:
#        return playlist #empty list
#    else:
#        playlist.append(songs[0][0])
#        size += songs[0][2]
#        del songs[0]
#
#        while True and songs != []:
#            (name,len,sn_size) = min(songs, key = lambda x: x[2])
#            size += sn_size
#            if size <= max_size:
#                playlist.append(name)
#                songs.remove((name,len,sn_size))
#            else:
#                break
#    
#    return playlist

#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#max_size = 12.2
#print(song_playlist(songs, max_size))
#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#max_size = 11
#print(song_playlist(songs, max_size))


#def greedySum(L, s):
#    """ input: s, positive integer, what the sum should add up to
#        L, list of unique positive integers sorted in descending order
#        Use the greedy approach where you find the largest multiplier for
#        the largest value in L then for the second largest, and so on to
#        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
#        return: the sum of the multipliers or "no solution" if greedy approach does
#        not yield a set of multipliers such that the equation sums to 's'
#        """
#
#    m = list(range(0,100))
#    mList = []
#    totalS = 0
#    
#    if L == []:
#        return 'no solution'
#
#    for j in range(len(L)):
#        for i in m:
#            if (totalS+L[j]*m[i]) > s:
#                mList.append(m[i-1])
#                totalS += L[j]*(m[i-1])
#                break
#    if totalS == s:
#        return sum(mList)
#    else:
#        return 'no solution'
#
#
#print(greedySum([10, 7, 6, 3], 19))

#def max_contig_sum(L):
#    """ L, a list of integers, at least one positive
#        Returns the maximum sum of a contiguous subsequence in L """
#    maxsofar = 0
#    maxendinghere = 0
#    for s in L:
#        # invariant: maxendinghere and maxsofar are accurate
#        # are accurate up to s
#        maxendinghere = max(maxendinghere + s, 0)
#        maxsofar = max(maxsofar, maxendinghere)
#    return maxsofar
#
#print(max_contig_sum([3, -3, 3, -3]))


