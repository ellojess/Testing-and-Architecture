# Debug Log

**Explain how you used the VSCode debugger tools to uncover the bugs in Exercise 7. Be specific. What breakpoints did you set? Where did you step to? What made you realize the error?**

_Example: I set a breakpoint on line 5 and stepped until line 12. There, I discovered that the `x` variable had a value of `-3`, whereas it should have had a value of `7`. That made me realize that we should be adding the two numbers `x` and `y`, instead of subtracting._

[[Your answer goes here!]]
I set a break point on line 10 and stepped through twice to see that the variable `start_str` was still set at "okay" even though "fantastic" was assigned to the `result`. I also noticed that instead of returning the full sentence, only "fantastic" would get returned. From here I decided to evaluate the return statements and found we were using `start_str` where we should have been using `sentence`

