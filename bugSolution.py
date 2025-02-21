def function_with_uncommon_error_solution(x, y):
    if y == 0:
        return "Error: Division by zero"
    elif x == 0:
        return y
    else:
        return x / y

result = function_with_uncommon_error_solution(10, 0)
print(result) # Output: Error: Division by zero
result = function_with_uncommon_error_solution(0, 10)
print(result) # Output: 10
result = function_with_uncommon_error_solution(10, 2)
print(result) # Output: 5.0