import time
start_time = time.time()


# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

a = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# First create some parameters to carry data

index=0
adjacent_digits = 13
sum = 0
max_sum = 0
max_sum_start_index=0
# a = 123745688000   # Kept the original for practice

# Found this code for transforming an integer value into a list with individual digits on each list index.
# To string and back

p = str(a)
li = list(p)
s = []
for e in li:
    a = int(e)
    s.append(a)


n_index = len(s)                            # setting up a variable to list length.
n_range_index = n_index - adjacent_digits   # cutting of the index last digits.

for n in range (0, (n_index-adjacent_digits+1)): # for loop to go over the digits in the integer.
    sum=1                                   # resetting for each loop
    for i in range (0, adjacent_digits):    # for loop to picking the adjacent digits.

        sum = sum * s[n+i]
        # print(sum)
        if sum > max_sum:                   # Checking for the maximum sum of adjacent digits.
                max_sum = sum
                max_sum_start_index=n

print(max_sum)
print(max_sum_start_index)
# print(sum)
print(n_index)
# print(li)
# print(s)
print(s[max_sum_start_index:(max_sum_start_index+adjacent_digits)])
print("--- %s seconds ---" % (time.time() - start_time))  # got --- 0.0029904842376708984 seconds ---