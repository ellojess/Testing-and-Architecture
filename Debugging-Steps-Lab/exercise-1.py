"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
'''
Expecting there to be an int returned as the largest integer difference

In the example with list_of_nums being [5, 3, 1, 2, 6, 4]
The largest diff between consecutive numbers is between 2 and 6
The expected output should be 4

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
That means that the variable i is outside of the bounds of the list. 
We need to find out why i has a value that's 
greater than or equal to the length of the list.
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
'''
One of the first assumptions made is that the list_of_nums is not empty and therefore has a range of numbers (ints)
diff is made up of the absolute value of the difference between i (list_of_nums[i]) and the item immeditely following i (list_of_nums[i+1]))
Then if the diff in that instance is larger than the current largest_diff, then assign diff as the new largest_diff
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