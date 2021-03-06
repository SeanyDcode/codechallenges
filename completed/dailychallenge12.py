# from dailycodingproblem.com
#
# Daily Challenge #12
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write 
# a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of 
# positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def staircase(n, X):
    # create list for storing potential combinations for each step
    cache = [0 for _ in range(n + 1)]
    # initialize for step 1
    cache[0] = 1
    # add value for each step based on value for previous step
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    # return last value from list which is the total number of possible combinations
    return cache[-1]


def main():
    X = [1, 3, 5]
    n = 9

    # call recursive function to find uniqueCount of possible step combinations
    print(staircase(n, X))
    
    
if __name__ == "__main__":
    main()
