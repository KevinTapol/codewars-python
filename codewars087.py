# Sum of two lowest positive integers
# Parameters or Edge Cases:
    # input will be an array of positive integers
    # can the array be empty or null?
# Return:
    # the sum of the 2 lowest integers
# Examples:
    # [19, 5, 42, 2, 77] => 7
    # [10, 343445353, 3453445, 3453545353453] => 3453455
# Pseudo Code
    # sort the array from lowest to highest 
    # return the sum of the first and second indexes
# my answer
def sum_two_smallest_numbers(numbers):
    arr = sorted(numbers)
    return arr[0] + arr[1]

# my answer refactored implicit return
sum_two_smallest_numbers = lambda a: sorted(a)[0] + sorted(a)[1]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77])) # 7
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])) # 3453455

# best practices and most clever
# sort the array the make a shallow copy ending at the 2nd element then sum the new array
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# using .sort() instead of sorted 
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]

# looping through the array and assigning the smallest and would break for 0 or falsy
def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None 
    for n in numbers: 
        # if at first None or element is less than var
        if not smallest1 or n < smallest1: 
            smallest2 = smallest1
            smallest1 = n 
        elif not smallest2 or n < smallest2: 
            smallest2 = n 
    return smallest1 + smallest2

# grab first min() and remove from array then grab min() after removed and sum them
def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min

# same idea as above but using array methods to pop or remove the min value from the array and using min again
def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))

# importing to use nsmallest(number of elements, array)
import heapq
def sum_two_smallest_numbers(numbers):
    return sum(heapq.nsmallest(2, numbers))

# using filter to create a shallow copy of the input array and remove any values equal to or less than 0
sum_two_smallest_numbers = lambda A: sum( sorted( filter( lambda x:x>0, A) )[:2] )

# same as above but using for elements in array
def sum_two_smallest_numbers(numbers):
    integer_arr = [x for x in numbers if isinstance(x, int) and x >= 0]
    return sum(sorted(integer_arr)[:2])

# I forgot in python range(start, stop, step)
def sum_two_smallest_numbers(numbers):
    lowest_num1 = numbers[0]
    index = 0
    for i in range(0,len(numbers)):
        if lowest_num1 > numbers[i]:
            lowest_num1 = numbers[i]
            index = i
    numbers.pop(index)
    lowest_num2 = numbers[0]
    for i in range(0,len(numbers)):
        if lowest_num2 > numbers[i]:
            lowest_num2 = numbers[i]
            index = i;
    return lowest_num1 + lowest_num2

# sorting the list from lowest to highest with .sort(reverse=True) then remove the last two elements one at a time with .pop() and add them
def sum_two_smallest_numbers(numbers):
    #your code here
    number=numbers #lol
    number.sort(reverse=True)
    a=number.pop()
    b=number.pop()
    return a+b

# getting min(array) and next min(array not equal to min(array))
def sum_two_smallest_numbers(numbers):
    return min(numbers) + min([i for i in numbers if i != min(numbers)])

# start is inclusive but stop is exclusive meaning to get index 0 and index 1 start at index 0 and end at index 2
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])

# using enumerate index elements
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    for i, item  in enumerate(numbers) : 
        if item > 0 : 
            if i < len(numbers): 
                return numbers[i] + numbers[i+1]
            
# nested for loop
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    for i in numbers[:1]:
        for j in numbers[1:2]:
            return i + j
