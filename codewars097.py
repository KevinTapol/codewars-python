# Sum of odd numbers
# Parameters or Edge Cases:
    # inputs will be an integer representing row of 
# Return:
    # the sum of the odd numbers given the input row number
# Examples:
    #                 1
    #              3     5
    #           7     9    11
    #       13    15    17    19
    #    21    23    25    27    29
    
    # 1 => 1
    # 2 => 8
    # 13 => 2197
    # 19 => 6859
    # 41 => 68921
    # 42 => 74088
    # 74 => 405224
    # 86 => 636056
    # 93 => 804357
    # 101 => 1030301

# Pseudo Code:
    # I remember this from before and I know it is n to the power of 3.
    # When I solved this from scratch before, I found the first value of n*(n-1) + 1 and created a new array start from first value stop at length of input and step by 2. Then I summed the array. 
    # Guass sum 1 to n = n(n+1)/2
    # n*(n-1) +1 = first integer in row
    # input integer represents both the row number and the number of integers to add

    # create an array with the first integer with length of input/row num step by 1
    # return the sum of the array

# my answer, best practices and most clever
# Then the sum in the n-th line is [2S+1] + [2(S+1)+1] + [2(S+2) + 1] + .... + [2(S+(n-1)) + 1] = n + n*(2S) + 2(1+2+...+(n-1)) = n + n*(n-1)n + 2 (n-1)*n/2 = n + n^3 -n^2 + (n-1)*n = n + n^3 - n^2 + n^2 - n = n^3
#  [1 + n*(n-1) + 1+(n+1)* n-2 ]*n/2 = n^3;
def row_sum_odd_numbers(n):
    return n**3

# # my answer refactored implicit return
row_sum_odd_numbers = lambda n: n**3

# my answer creating a new list with Gauss sum 1 to n = n(n+1)/2 range(start, stop, step)
def row_sum_odd_numbers(n):
    first_val = n*(n-1) + 1
    last_val = n*(n+1)
    x = range(first_val, last_val, 2)
    return sum(x)

# my answer creating new list refactored implicit return
row_sum_odd_numbers = lambda n: sum(range(n*(n-1) + 1, n*(n+1), 2))

print(row_sum_odd_numbers(1)) # 1
print(row_sum_odd_numbers(2)) # 8

# using pow(input, 3) for input to the power of 3
def row_sum_odd_numbers(n):
    return pow(n, 3)

# using %2 as a condition
def row_sum_odd_numbers(n: int):
    """ Calculate the row sums of this triangle from the row index (starting at index 1). """
    return sum([_ for _ in range(n * (n - 1), n * (n - 1) + (n * 2)) if _ % 2])

# for loop using range
def row_sum_odd_numbers(n):
    sum = 0
    num = n * n + n - 1
    for i in range(n):
        sum += num
        num -= 2
    return sum

# declared empty list and appended each index starting at 1 then create another list and subtract the values up to n to get only the single row at n and sum that row/array
def row_sum_odd_numbers(n):
    #your code here
    x = []
    for i in range(1,n*n+n,2):
        x.append(i)
    return sum(x[-n:])