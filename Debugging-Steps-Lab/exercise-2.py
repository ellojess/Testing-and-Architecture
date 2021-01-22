"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
'''
Expected:
### Problem 2 ###
False 
True 

Actual: 
### Problem 2 ###
False
False
'''
# - What error message (if any) is there?
'''
No error message but the outputs are not as expected
'''
# - What line number is causing the error?
'''
Likely the first if statement (lines 44-45)
'''
# - What can you deduce about the cause of the error?
'''
There is a lapse in logic in the first if statement which results in an early return False 
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
'''
One of the first assumptions made is that the list_of_nums is not empty and has at least 3 items(ints) in it

Then check if (list_of_nums[i+1] == list_of_nums[i] + 1 and list_of_nums[i+2] == list_of_nums[i] + 2):

[1, 2, 4]    first iteration: 2 = 2 and 4 = 3 return FALSE 
    ^  ^

After the false statement, we exit the loop to return False once more 
'''

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True