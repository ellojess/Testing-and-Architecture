"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
'''
Expected:
an int to be returned that is the index of the given element 
within the array by performing a binary search.


Actual: 
Error message: 
'''
# - What error message (if any) is there?
'''
  File "exercise-4.py", line 32
    if high == None:
                   ^
IndentationError: unindent does not match any outer indentation level
'''
# - What line number is causing the error?
'''
In the error message it states that the problem is occurring on line 32 
'''
# - What can you deduce about the cause of the error?
'''
Moving forward with fixing the error on line 32, I can assume it will jump to
all following lines and that the indentation will need to be fixed for the entirety of the code base 
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
'''

'''

def binary_search(arr, element, low=0, high=None):
      """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)