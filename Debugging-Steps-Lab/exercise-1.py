"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
'''
Expecting there to be an int returned as the largest integer difference
print 4, as the largest diff between consecutive numbers is between 2 and 6

Actual output is the following error message: 
'''
# - What error message (if any) is there?
'''
### Problem 1 ###
Traceback (most recent call last):
  File "exercise-1.py", line 42, in <module>
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])
  File "exercise-1.py", line 34, in find_largest_diff
    diff = abs(list_of_nums[i] - list_of_nums[i+1])
IndexError: list index out of range
'''
# - What line number is causing the error?
'''
According to the traceback message the error is on line 34
'''
# - What can you deduce about the cause of the error?
'''
This means that there are invalid indecies 
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
'''
Assumption is that there will be an index out of range error 
'''

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)