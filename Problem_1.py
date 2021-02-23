###  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

### Find the sum of all the multiples of 3 or 5 below 1000.

# First define variables that can be used later on
factor_a = 3
factor_b = 5
n = 0
multiplies_a = 0
multiplies_b = 0

#Use list to store the result of the multiplies

multiplies_list = []

#Set the roof level for resulting multiplies
multiplies_max = 1000

# First make a list with while loop for the largest factor
while multiplies_b < multiplies_max:

  n += 1
  multiplies_list.append(multiplies_b)
  multiplies_b = factor_b * n


#Reset the n counter variable to 0
n = 0

# Continue to add values to the list for the smaller factor.
while multiplies_a < multiplies_max:

  # if condition is to eliminate that equal multiplies from factor a and b added to the list
  n += 1
  if multiplies_a not in multiplies_list:
    multiplies_list.append(multiplies_a)
  multiplies_a = factor_a * n


print(multiplies_list)

#Manual way to summarize the multiplies with a list_sum variable
list_sum=0

for x in multiplies_list:
    list_sum += x

print(list_sum)

#using built in sum function for list to display answer
print(sum(multiplies_list))