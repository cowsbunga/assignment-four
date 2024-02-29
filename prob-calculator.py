import numpy as np
import math

n = int(input("Enter the step number: ")) - 1
low_bound = math.ceil(n/2)
sum = 0

for k in range(low_bound, n+1):
    term = math.comb(k, n-k) * pow(2, n-k)
    sum += term

            
prob = sum / pow(2, n)
print("probability: ", prob)