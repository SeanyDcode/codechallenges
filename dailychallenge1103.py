# from dailycodingproblem.com
#
# Daily Challenge #1103
#
# You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are 
# there to reach the bottom right corner?
#
# You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot 
# walk through.
#
# For example, given the following matrix:
#
# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]
# Return two, as there are only two ways to get to the bottom right:
# 
# Right, down, down, right
# Down, right, down, right
# The top left corner and bottom right corner will always be 0.
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
