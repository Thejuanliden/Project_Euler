# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


# Yet another brute force. Need to get back into math studies.
# Hopefully get some inspiration for where to start from the problem overview.
# I have a feeling later problems will be extremely difficult without that math knowledge boost.
# Buy hey I''m here to learn :)

count = 0
n=2
target_value = 10001
target_prime = 0
top = 1000000 # this one I estimated (not proud)
prime=[]


# prime number generation
for n in range(2, top):

    for x in range(2,n):

        if n % x == 0:

            # print(top)
            break
    else:

        target_prime = n
        count += 1 # when a prime number is identified the counter adds 1.


    if count == target_value: # when target prime n is reached the counter stops the for loop.
        break

print(count)
# print(prime)
print(target_prime)
