"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
'''
Expected: output of a sorted array 
example: [5, 2, 3, 1, 6] -> [1, 2, 3, 5, 6]

Actual output is the following error message:
'''
# - What error message (if any) is there?
'''
### Problem 3 ###
Traceback (most recent call last):
  File "exercise-3.py", line 45, in <module>
    answer = insertion_sort([5, 2, 3, 1, 6])
  File "exercise-3.py", line 37, in insertion_sort
    while key < arr[j] : 
IndexError: list index out of range
'''
# - What line number is causing the error?
'''
According to the traceback message the error is on line 37
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
# HINT: It may help to draw a picture to clarify what your assumptions are.
'''
One of the first assumptions made is that the arr is not empty and therefore has a range of numbers (ints)

Move items that are greater than the key, ahead of the current position then, continue until sorted and return the sorted array
'''

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

