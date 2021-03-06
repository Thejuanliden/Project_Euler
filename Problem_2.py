#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# a + b = fib_num

#First create some variables with starting values for the sequence
a = 0
b = 1
fib_num = 0
#Create two lists, one to store the complete sequence up to four million term and one to only store even terms. List are not needed but nice visual part.
fib_list=[]
fib_list_even_num=[]
#The fib_sum_even is the only variable needed to solve the problem.
fib_sum_even = 0

max_fib_term = 4000000

#The while loop to calculate the fibonacci sequence up to four million as long as fib_num is less than four million.
while fib_num < max_fib_term:
    fib_num = a + b
    a = b
    b = fib_num
    fib_list.append(fib_num) #append to the list for the complete sequence (not needed for the solution)
    if fib_num % 2 == 0: #condition to check for even numbers and then store them to either even number list or fib_sum_even.
        fib_list_even_num.append(fib_num)
        fib_sum_even += fib_num

#Print operations to view the data generated.
print(fib_list)
print(fib_list_even_num)
print(fib_sum_even)
print(sum(fib_list_even_num))
