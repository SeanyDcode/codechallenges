#  from dailycodingproblem.com
#
# Daily Challenge #1101
# Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, 
# find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.
#
# Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.
#
# For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.
# 
# Response by Claude
# Here is one way to solve this problem in Python:

import math

def assign_mice_to_holes(mice, holes):
  
  # Sort the mice and hole positions
  mice.sort()
  holes.sort()

  # Initialize result variable
  max_distance = 0

  # Iterate through mice and assign to closest hole
  for i in range(len(mice)):
    mouse = mice[i]
    hole = holes[i]
    
    # Calculate distance 
    distance = abs(mouse - hole)
    
    # Update max distance if needed
    max_distance = max(max_distance, distance)
    
  return max_distance


# The key steps are:
#
# 1. Sort the mice and holes arrays so they are in ascending order. This allows us to iterate through them together easily.
#
# 2. Initialize a `max_distance` variable to track the largest steps any mouse takes. 
#
# 3. Loop through the mice and holes together. For each mouse, find its closest hole and calculate the distance.
#
# 4. Update `max_distance` if the current distance is larger. 
#
# 5. Return `max_distance` after checking all mice.
#
# The time complexity is O(NlogN) due to sorting, and space is O(1).
#
# Let me know if you have any other questions!
