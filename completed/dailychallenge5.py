# From dailycodingproblem.com
#
# Daily Challenge #5
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#    def pair(f):
#        return f(a, b)
#    return pair
#
# Implement car and cdr.

def car(result):
    def first(a, b):
        return a
    return result(first)
  
def cdr(result):
    def second(a, b):
        return b
    return result(second)
    
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

print(f"First element: {car(cons(3, 4))}")
print(f"Second element: {cdr(cons(3, 4))}")
