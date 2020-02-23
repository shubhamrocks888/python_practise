import random
# value = random.random()
# print(value)               ---> 0.7990680558266642  --> gives a random floating value between 0 and 1

# value = random.uniform(1,10)
# print (value)  ---->  7.014714037466076  ---> gives a random floating value between two numbers

# value = random.randint(1,6)
# print (value) ---> gives a a random int value between two numbers (two numbers are inclusive)

# value =  ["monty",'mayank','anni','chaudhary']
# print (random.choice(value))  ---> gives a random value among list ot tuple values

# value =  ["monty",'mayank','anni','chaudhary']     --> here,k = number of values you want to print and weights is the probability of the values to be printed
# print (random.choices(value,weights=[1,1,1,1],k=4))       default value of k and weights is 1
# here, it does not pick unique values

# value = list(range(1,53))  --> [1,2,3------,52]
# random.shuffle(value) --->shuffling the values of list
# print (value) ---->    [29, 48, 16, 50, 26, 27, 6, 35, 25, 2-----]

# value = list(range(1,53))
# hand = random.sample(value,k=5)  ---> select 5 unique values
# print (hand)          ---->       [22, 12, 51, 25, 3]

