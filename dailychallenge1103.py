# from dailycodingproblem.com
#
# Daily Challenge #1103
#
# There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are 
# no gaps between any of them, while keeping overall movement to a minimum.
#
# For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 
# 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can 
# consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.
#
# Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
#
# Response from Claude
# Here is one way to solve this using dynamic programming in Python:

def num_ways(matrix):
  # Get matrix dimensions
  n = len(matrix)
  m = len(matrix[0])
  
  # Create DP table filled with 0s
  dp = [[0 for _ in range(m)] for _ in range(n)]
  
  # Ways to reach first cell = 1
  dp[0][0] = 1
  
  # Iterate rows
  for i in range(n):
    # Iterate cols 
    for j in range(m):
      
      # Skip first cell
      if i == 0 and j == 0: 
        continue
        
      # Check if current cell is open  
      if matrix[i][j] == 0:
      
        # Add number of ways to reach cell above
        if i > 0:
          dp[i][j] += dp[i-1][j]
          
        # Add number of ways to reach cell to left  
        if j > 0:
          dp[i][j] += dp[i][j-1]
        
  # Bottom right has total number of ways          
  return dp[-1][-1] 

# The key ideas are:
#
# - Initialize a DP table to store number of ways to reach each cell
# - Iterate through the matrix, at each cell adding:
#   - Ways to reach directly above
#   - Ways to reach directly left
# - Return bottom right cell's value
#
# This tabulates the results in a bottom-up fashion to efficiently calculate the final ways to the destination.
#
# Time and space complexity is O(NM) from the DP table.
