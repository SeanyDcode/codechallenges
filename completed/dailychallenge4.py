# From dailycodingproblem.com
#
# Daily Challenge #4
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

array = [3, 4, -1, 1]

def lowest_pos(array):
    
    # declare lowest_int
    lowest_int = 1
    
    # iterate through array
    for i in range(len(array)):
        
        # pass if negative, 0, or lowest_int already less than current array item
        if array[i] <= 0 or array[i] > lowest_int:
            pass
          
        # if item equals current lowest_int, increase by 1
        else:
            lowest_int += 1
            
    return lowest_int            
    
print(lowest_pos(array))
