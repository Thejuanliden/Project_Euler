#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#prime_number = 600851475143
target = 600851475143
#first create an empty list to store all the prime factors in.
prime_factor_list = []

for n in range(2,target):
    for x in range (2,n):
        if n % x == 0:
            break
    if target % n == 0: # check if target can be divided by the prime factor n.

        # store the prime factory in the list.
        prime_factor_list.append(n)

        # adjust the target by dividing with the identified prime factor.
        target = target / n

        # check if adjusted target can be divided by the identified prime factor multiple times.
        while target % n == 0:
            prime_factor_list.append(n)
            target = target / n

    elif target == 1:
        break
print(prime_factor_list)
