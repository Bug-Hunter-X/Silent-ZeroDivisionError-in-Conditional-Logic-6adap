# Silent ZeroDivisionError in Conditional Logic

This code demonstrates a subtle error that can occur in conditional logic when dealing with potential division by zero. The error is not immediately obvious because the `ZeroDivisionError` is only thrown if a specific condition is not met.

The `function_with_uncommon_error` function attempts to handle division by zero by checking if either `x` or `y` is zero. However, the logic is flawed. If `x` is not zero but `y` is, the `elif` condition is skipped, and the function proceeds to `x / y` causing the error to occur silently.

## Reproducing the Error

1. Execute `bug.py`
2. Observe that the error only occurs when both x and y are not 0. But if x is 0, the function returns y, and if y is 0 but x isn't 0, the ZeroDivisionError still occurs.

## Solution

The `bugSolution.py` file provides a solution to correct this logic. This solution uses a more robust method to handle potential division by zero. It explicitly checks if `y` is zero before performing the division. If `y` is zero, an appropriate error message is returned. 