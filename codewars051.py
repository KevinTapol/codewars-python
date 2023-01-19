# Count by X
# Parameters or Edge Cases:
    # inputs will be integers greater than 0
# Return:
    # an array/list length equal to the second input where the each value is the first input multiplied by 1 at index 0 incrementing by 1 per each index
# Examples:
    #   count_by(1, 5), [1, 2, 3, 4, 5]
    #   count_by(2, 5), [2, 4, 6, 8, 10]
    #   count_by(3, 5), [3, 6, 9, 12, 15]
    #   count_by(50, 5), [50, 100, 150, 200, 250]
    #   count_by(100, 5), [100, 200, 300, 400, 500]
# Psuedo Code:
    # return a new array/list where the start value is the first input x the stop is (n + 1)*x (since array/list index starts at 0) and increment by the first input x

# my answer
def count_by(x, n):
    # return a new array/list where the start value is the first input x the stop is (n + 1)*x (since array/list index starts at 0) and increment by the first input x
    return list(range(x, (n+1)*x, x))

# my answer refactored to lambda implicit return one line function
count_by = lambda x,n: list(range(x, (n+1)*x, x))

print(count_by(1, 5)) # [1, 2, 3, 4, 5]
print(count_by(2, 5)) # [2, 4, 6, 8, 10]
print(count_by(3, 5)) # [3, 6, 9, 12, 15]
print(count_by(50, 5)) # [50, 100, 150, 200, 250]
print(count_by(100, 5)) # [100, 200, 300, 400, 500]

# best practices and most clever imo Creating a list with a range is better practice than a for loop
# here they are using [] to return an array and the increment is i*x but start at 1 because 0*x = 0
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

# while loop
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    output = []
    i = 1
    while len(output) < n:
        output.append(i*x)
        i += 1
    return output

# adding 1 to the product of the inputs instead of adding 1 to n then multiply by x
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return list(range(x, n * x + 1, x))

# using array/list methods
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    num = x
    results = [x]

    for i in range(n-1):
        num += x
        results.append(num)

    return results

# using enumerate(iterable object, start default 0) function takes a collection (e.g. a tuple) and returns it as an enumerate object.
def count_by(x, n):
    return [x *  index for index, item in enumerate(range(n),1)]