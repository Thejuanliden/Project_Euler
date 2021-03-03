import time
start_time = time.time()

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

# starting of with some empty list (not needed in the end but good during development) and variable.

palindromic_numbers = []
largest_palindromic = 0

for n in range (100,999):
    for x in range (100, 999):
        num = x * n
        number = num
        revs_number = 0

        # reverse the number and then check if subtraction is resulting in zero, that way we can determine if we have a palindromic number.
        while (number > 0):

            # Logic
            remainder = number % 10
            revs_number = (revs_number * 10) + remainder
            number = number // 10
            #print(revs_number)
        #print(revs_number)

        if num - revs_number == 0:

            # created a list to save the palindromic values during code development.
            palindromic_numbers.append(revs_number)
            palindromic_numbers.append(x)
            palindromic_numbers.append(n)

            # if discovered palindromic value is larger than previous value it replace it.
            if largest_palindromic < revs_number:
                largest_palindromic = revs_number

#print(palindromic_numbers)
print('Largest palindromic number:')
print(largest_palindromic)
print("--- %s seconds ---" % (time.time() - start_time))