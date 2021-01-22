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

Actual output is the following error message:
'''
# - What error message (if any) is there?
'''
  File "exercise-4.py", line 62
    if high == None:
                   ^
IndentationError: unindent does not match any outer indentation level

After fixing the indentation error on the line prior to it, we get the following Traceback error: 

Traceback (most recent call last):
  File "exercise-4.py", line 82, in <module>
    answer = binary_search([1, 2, 4, 5, 7], 7)
  File "exercise-4.py", line 78, in binary_search
    return binary_search(arr, element, mid, high)
  File "exercise-4.py", line 78, in binary_search
    return binary_search(arr, element, mid, high)
  File "exercise-4.py", line 78, in binary_search
    return binary_search(arr, element, mid, high)
  [Previous line repeated 995 more times]
  File "exercise-4.py", line 63, in binary_search
    if high == None:
RecursionError: maximum recursion depth exceeded in comparison
'''
# - What line number is causing the error?
'''
In the error message it states that the problem is begins on line 63
'''
# - What can you deduce about the cause of the error?
'''
There is a stack overflow; may need to set a higher recursion depth
or optimize tail recursion 
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
'''
One of the first assumptions made is that the arr is not empty and is already sorted 
Another being the element being searched for will always exist in the array somewhere since there is no edge case handling it 
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

    # If element is less than mid then it will be in left subarray 
    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        # else it will be in right subarray 
        return binary_search(arr, element, mid, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)