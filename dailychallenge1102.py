# from dailycodingproblem.com
#
# Daily Challenge #1102
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
# Here is one approach in Python:

def minimize_gaps(seats):
  # Track number of people and total cost
  num_people = sum(seats) 
  cost = 0
  
  # Start seat index at 0
  seat_idx = 0
  
  for i in range(len(seats)):
    if seats[i] == 1:
      # Person encountered, move them to next seat if needed
      move_distance = abs(seat_idx - i)
      cost += move_distance
      
      # Increment seat index
      seat_idx += 1 
      
  return cost


# The key steps are:
#
# 1. Iterate through the seat array. 
# 2. When a person is encountered, calculate the distance to move them to the next open seat index.
# 3. Add this distance to the total cost.
# 4. Increment the seat index to keep track of where the next open seat is.
#
# This greedy approach minimizes cost by moving each person as little as possible to the next open seat.
#
# The time complexity is O(N) since we traverse the seats array once. The space complexity is O(1) as we 
# only use a constant number of extra variables.
