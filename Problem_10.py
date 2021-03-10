import time

start_time = time.time()
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

target = 2000000
# first create an empty list to store all the prime factors in.
prime_list = [2,3]
sum_of_primes = 2
a = 0
b = 0
count = 10

# tried by using the prime_list as a sieve and running through every odd number from 3 up to target. For every new prime number found it is added to the sieve.
# it takes considerable time to go through all number up to 2 million. The solution from project euler is too abstract for me yet. Need to come back to that when I caught up on the math.

for n in range(3,target,2):
    for i in (prime_list):
        if n % i == 0:
            #print(f'B n:{n} i:{i}')

            break
    else:
        prime_list.append(n)

        #print(n)

print(f'# of primes:{len(prime_list)}')
print(f'# of primes:{sum(prime_list)}')
print(prime_list[-1]) #1999993

# of primes:148933
# of primes:142913828922

#--- 613.0176165103912 seconds ---



print("--- %s seconds ---" % (time.time() - start_time))  # got --- x seconds ---