# From dailycodingproblem.com
#
# Daily Challenge 2
# Given and array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If your input was [3, 2, 1], the expected output would be [2, 3, 6].

array = [1, 2, 3, 4, 5]

def product_array(array):
    
    output = []

    # iterate through items in array
    for i in range(len(array)):
        counter = 0
        product = 1
  
        # iterate through 
        while counter < len(array):
            # don't update product for ith item in array
            if i != counter:
                product *= array[counter]
    
            # update counter
            counter += 1
        
        # append final product to output array
        output.append(product)

    # return product array
    return output

print(product_array(array))
