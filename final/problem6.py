import numpy as np

def find_combination(choices, total):
    """
        choices: a non-empty numpy.array of ints
        total: a positive int
        
        Returns result, a numpy.array of length len(choices)
        such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
        In case of ties, returns any result that works.
        If there is no result that gives the exact total,
        pick the one that gives sum(result*choices) closest
        to total without going over.
        
        list is NOT sequential
        
        possibility:
        create ALL possible choices
        check for ones that match total
        
        """
    all_combos = []
    bestsize = len(choices)
    total_not_found = True
    for i in powerSet(choices):
        all_combos.append(i)
    for i in all_combos:
        currentsum = 0
        currentsize = 0
        for index, value in enumerate(i, 0):
            if value == 1:
                currentsize += 1
                currentsum += choices[index]
        if currentsum == total:
            if currentsize <= bestsize:
                bestsize = currentsize
                total_not_found = False
                bestcombo = i
        elif currentsum < total and total_not_found:
            if currentsize <= bestsize:
                bestcombo = i
    return(np.array(bestcombo))


def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            # if (i >> j) % 2 == 1:
            #     combo.append(items[j])
            combo.append((i >> j) % 2)
        yield combo

#print(find_combination([3, 10, 2, 1, 5], 12))
#print(find_combination([1, 3, 4, 2, 5], 16))
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171))
