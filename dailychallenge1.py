# From dailycodingproblem.com
#
# Daily Challenge 1
# Given a list of numbers and number k, return whether any two numbers from the list add up to k.
#
# For example, give [10, 15, 3, 7] and k of 17, return true since 10 + 7 = 17.

array = [10, 15, 3, 7]
k = 17

def check_total(array, k):

    length = len(array)

    # iterate through all array values except last one
    for i in range(length - 1):
  
        # initialize counter for comparing other values in array with current value
        j = i + 1
  
        # find remainder to compare to other array values 
        remainder = k % array[i]
  
        # iterate through other values after ith value in array
        while j < length:
  
            # if remainder matches another value in array, return True
            if remainder == array[j]:
                return True
    
            j += 1

    return False

print(check_total(array, k))
