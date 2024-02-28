#finds the probability of landing on step n in a number path, by summing all possible combinations that involve landing on n, and diving by the total number of possible combinations

import numpy as np
import math

def simplify_fraction(numerator, denominator):
    if math.gcd(numerator, denominator) == denominator:
        return int(numerator/denominator)
    elif math.gcd(numerator, denominator) == 1:
        return str(numerator) + "/" + str(denominator)
    else:
        top = int(numerator / math.gcd(numerator, denominator))
        bottom = int(denominator / math.gcd(numerator, denominator))
        return str(top) + "/" + str(bottom)
    

n = int(input("Enter the step number: "))
flips = [1]*(n-1)
possible_combos = 0


for i in range(pow(2, n-1)):

    #finds out if the current combination will involve landing on n
    for j in range(1, n):
        if np.sum(flips[:j]) == n:
            possible_combos += 1
            break

    #iterates to the next combination    
    for k in range(n-1):
        if flips[k] == 1:
            flips[k] = 2
            for x in range(0, k):
                flips[x] = 1
            break

#calculates probability
print("probability = ", simplify_fraction(possible_combos, pow(2, n-1)))