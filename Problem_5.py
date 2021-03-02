#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# not to proud of this brute force attack. Got the right answer but not the analytical way described in the solution.
# this uses up a lot of cpu resources and it takes some time to get the answer. I'm learning so I settle for now but might come back and redo.

# used a list so that I can stop after the length of the list changes from zero to one
x=[]
n=0

while len(x) < 1:
    n += 1
    # checking if n is evenly dividable by all these numbers. Not pretty at all but got the job done.
    if n%1==0 and n%2==0 and n%3==0 and n%4==0 and n%5==0 and n%6==0 and n%7==0 and n%8==0 and n%9==0 and n%10==0 and n%11==0 and n%12==0 and n%13==0 and n%14==0 and n%15==0 and  n%16==0 and n%17==0 and  n%18==0 and n%19==0 and n%20==0:
        x.append(n)


print(x)


