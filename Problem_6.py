#The sum of the squares of the first ten natural numbers is, 385

#The square of the sum of the first ten natural numbers is,     3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#some parameters
sum_of_squares =0
sum_of_numbers=0
square_of_sum=0
i_list=[]
diff = 0

first_natural_numbers= 100

#for loop with the range

for i in range(1, (first_natural_numbers+1)):
    sum_of_squares += i*i
    sum_of_numbers += i
    i_list.append(i)

square_of_sum = sum_of_numbers * sum_of_numbers
diff = square_of_sum - sum_of_squares

#the elegant solution from project euler:
# limit = 100
# sum = limit(limit + 1)/2
# sum sq = (2limit + 1)(limit + 1)limit/6
# print sum2 − sum sq

sum_n = first_natural_numbers*(first_natural_numbers + 1)/2
sum_sq = (2*first_natural_numbers + 1) * (first_natural_numbers + 1)*first_natural_numbers/6


print( i_list[-1])
print(f'sum_n {sum_n}')
print(f'sum_of_numbers: {sum_of_numbers}')
print(f'sum_sq: {sum_sq}')
print(f'sum_of_squares: {sum_of_squares}')
print(f'difference: {diff}')
