# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

- What is the expected vs. actual output?
Expected: See new pizzas on home page

Actual: New pizzas aren't being added to the homepage

- If there is a stack trace, what useful information does it contain?
TypeError: 'topping' is an invalid keyword argument for PizzaTopping


- Which technique did you use, on which line numbers?
Used divide and conquer to see where 'topping' was being used 
Found location at: Line 79 
Led to finding that topping was not added as an attribute type and the form was only looking for crust and size. 
Also found a url redirect issue (line 84) which can possibly be fixed using the template name or by not using url_form. 
Afterwards it would seem that nothing was getting saved, this could be fixed by saving the items to the database with session.commit() 

- What assumptions did you have about each line of code, and which ones were proven to be wrong?
Initial assumption was that after submitting the form via the submit button, the user would be redirected to the home screen with the new order presented on the front page. They were all proven to be wrong with the given issues found listed in the previous question. 


## Exercise 2

- What is the expected vs. actual output?
Expected: Output of the weather in current city presented on the first page 

Actual: Submit button is broken so we do not get the output presented

- If there is a stack trace, what useful information does it contain?
Shows that there is invalid API key, then shows geo errors from Open Weather

- Which technique did you use, on which line numbers?
Trace back technique, found that the problem is on line 44
Issue was a result from there being no API key for Open Weather 
Afterwards there is a geo error because args users_city= should be city= line
Temperature should also be temp 
Naming parameter (city name) was also incorrect, according to the documentation from the API, city is q  so that should be updated as well.

- What assumptions did you have about each line of code, and which ones were proven to be wrong?
Made the assumption that the issue was due to there being no API key for Open Weather, after that was resolved, other errors appeared. Such as using the wrong names in params and args as listed above. 


## Exercise 3

- What is the expected vs. actual output?
Expected: Functional merge_sort and binary_search algorithms 

Actual: 
List of nums is:
[7, 4, 9, 3, 5, 6, 1, 2]
Traceback (most recent call last):
  File "/Users/jessicatrinh/Documents/Testing-and-Architecture/Debugging-Techniques-Lab/exercise-3/main.py", line 8, in <module>
    merge_sort(list_of_nums)
  File "/Users/jessicatrinh/Documents/Testing-and-Architecture/Debugging-Techniques-Lab/exercise-3/utils.py", line 16, in merge_sort
    merge_sort(left_side)
  File "/Users/jessicatrinh/Documents/Testing-and-Architecture/Debugging-Techniques-Lab/exercise-3/utils.py", line 16, in merge_sort
    merge_sort(left_side)
  File "/Users/jessicatrinh/Documents/Testing-and-Architecture/Debugging-Techniques-Lab/exercise-3/utils.py", line 37, in merge_sort
    arr[k] = right_side[i]
IndexError: list index out of range

- If there is a stack trace, what useful information does it contain?
Shows an IndexError: list index out of range

- Which technique did you use, on which line numbers?
Traceback technique, found the issue on line 37 for merge sort 
line 46 should be <= and not just < for binary search 

- What assumptions did you have about each line of code, and which ones were proven to be wrong?
merge_sort used the wrong variable (i instead of j) 
bianry search should use // instead of / 