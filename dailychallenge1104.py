# from dailycodingproblem.com
#
# Daily Challenge #1104
#
# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the 
# number could represent. You can assume each valid number in the mapping is a single digit.
#
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return 
# [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
#
# Response from Claude
# Here is one way to solve this using backtracking in Python:

def get_letter_combinations(digits, mappings):
  
  combinations = []
  
  def backtrack(index, path):
    # Base case
    if index == len(digits):
      combinations.append(''.join(path))
      return
    
    # Get possible letters for current digit
    letters = mappings[digits[index]]
    
    # Recursive case
    for letter in letters:
      path.append(letter)
      backtrack(index+1, path)
      path.pop()
      
  if digits: 
    backtrack(0, [])
  
  return combinations

# The recursive backtracking approach:
#
# - Takes the digit index and current path as arguments
# - Base case: when index reaches digits length, add path to combinations
# - Recursive case: 
#   - Get possible letters for current digit
#   - Append each letter to path 
#   - Backtrack on next index
#   - Pop letter off path after exploring
#
# This efficiently generates all combinations of letters that match the digit string.
#
# Time complexity is O(3^N * 4^M) where N is number of digits mapped to 3 letters, M mapped to 4 letters.
#
# Space complexity is O(3^N * 4^M) to store all combinations.
