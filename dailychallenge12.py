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

def recurseSteps(steps, strides, returnList):
    
    # if no steps remaining, return final list
    if steps == 0:
        return returnList
    
    # if steps remaining, continue to count step combinations
    else:
        
        # for each potential step combination
        for stride in strides:
            
            # CHECK FOR POTENTIAL DIVISION ABILITY WITH REMAINING STEPS
            
            # check to make sure stride is not larger than total steps remaining
            if steps - stride >= 0:
                # subtract stride from total steps remaining
                steps -= stride
                # add stride to returnList
                returnList.append(stride)
                # continue to recurse with function
                recurseSteps(steps, strides, returnList)
            else:
                pass


def main():
    uniqueLists = []
    x = [1, 2]
    n = 4

    # iterate through possible last steps
    for i in x:
      
      # call recursive function to find possible unique steps
      uniqueLists.append(recurseSteps(n, x, []))
    
    
    
  
if __name__ == "__main__":
    main()
