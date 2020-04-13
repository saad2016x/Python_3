

import math
print('Square root Program')
num = int(input("How many Numbers will be entered:"))
for i in range(num):
    n = int(input("Enter the  number: "))
    n_sqrt = int(math.sqrt(n))
    print(' The squarte root of',n,'is:',n_sqrt)
print('Done! Loop is Finish')