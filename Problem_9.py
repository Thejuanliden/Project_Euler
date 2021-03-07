import time
start_time = time.time()
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math # needed to import math to be able to use math.sqrt to do the square root of a number.

# First some parameters to start up with
target_sum_abc = int(1000)
a = 0
b = 0
c = 0
list_abc = [] # a nice list to visualise a, b, c.
product_abc = 0

for a in range (0, int(target_sum_abc)):
    for b in range (0, int(target_sum_abc / 2)):
        c = math.sqrt(a**2+pow(b,2))
        if (a + b + c) == target_sum_abc:
            list_abc.append(a)
            list_abc.append(b)
            list_abc.append(c)
            product_abc = a * b * c
            break
    if (a + b + c) == target_sum_abc:
        break

print(list_abc)
print(f'product abc: {product_abc}')














print("--- %s seconds ---" % (time.time() - start_time))  # got --- 0.0029904842376708984 seconds ---