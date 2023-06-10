# Consecutive strings
"""
    You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

    Examples:
    strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

    Concatenate the consecutive strings of strarr by 2, we get:

    treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
    folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
    trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
    blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
    abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

    Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
    The first that came is "folingtrashy" so 
    longest_consec(strarr, 2) should return "folingtrashy".

    In the same way:
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
    n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

    Note
    consecutive strings : follow one after another without an interruption
"""
# Parameters or Edge Cases:
"""
    first input will be an array of strings
    the array can be empty or null
    the strings can be letters, numbers or special characters
    second input will be an integer can be positive or negative
"""
# Return:
"""
    if k is greater than the length of the input array then return an empty string
    if k is less than 1 return an empty string
    return the first longest string consisting of k consecutive strings taken in the array without using the same element
"""
# Examples:
"""
    ["zone", "abigail", "theta", "form", "libe", "zas"], 2 => "abigailtheta"
    ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1 => "oocccffuucccjjjkkkjyyyeehh"
    [], 3) => ""
    ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2 => "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    ["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2 => "wlwsasphmxxowiaxujylentrklctozmymu"
    ["zone", "abigail", "theta", "form", "libe", "zas"], -2 => ""
    ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3 => "ixoyx3452zzzzzzzzzzzz"
    ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15 => ""
    ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0 => ""
"""
# Pseudocode:
"""
    # if k is less than 1 or greater than the length of the input array return an empty string
    # declare a string copy of the input array from index 0 to index k
    # grab k elements from the copy and concatenate them to result
    # convert result into a string with no spaces
    # return result 
"""
"""# NOTE I initially didn't see the key word CONSECUTIVE and thought to use array.sort(key=len, reverse=True). To use this, you need to maintain the same input all throughout and cannot change array name. Then convert them into a string. I want to show just the .sort() mechanic alone here.
EX
x = ["zone", "abigail", "theta", "form", "libe", "zas"]
x.sort(key=len, reverse=True)
print(x[:3])
will print to the console ['abigail', 'theta', 'zone']

arr = ["zone", "abigail", "theta", "form", "libe", "zas"]
x = arr.sort(key=len, reverse=True)
print(x[:3])
will print to the console None with the error object not subscriptable
"""
# my answer
def longest_consec(arr, k): 
    # if k is less than 1 or greater than the length of the input array return an empty string
    if k < 1 or k > len(arr):
        return ''
    # declare a string copy of the input array from index 0 to index k
    result = ''.join(arr[:k])
    # enumerate through the input array index and values
    for i,e in enumerate(arr):
        # if the length of result is less than the length of the current index string copy of the input array from the current index to the current index plus k then reassign result to the current index string copy from current index to current index plus k
        if len(result) < len(''.join(arr[i:k + i])):
            result = ''.join(arr[i:k + i])
    # outside of the for loop return result
    return result

# my answer refactored
def longest_consec(arr, k): 
    if k < 1 or k > len(arr):
        return ''
    result = ''.join(arr[:k])
    for i,e in enumerate(arr):
        if len(result) < len(''.join(arr[i:k + i])):
            result = ''.join(arr[i:k + i])
    return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)) # "abigailtheta"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)) # "oocccffuucccjjjkkkjyyyeehh"
print(longest_consec([], 3)) # ""
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) # "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)) # "wlwsasphmxxowiaxujylentrklctozmymu"
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)) # "abigailtheta"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)) # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)) # ""

# best practices
# very similar to my answer but using the global variable for empty string return
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

# most clever
# max(key=len) on the list of possible combination
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

# using range(key=len, reverse=True)
def longest_consec(s, k):
    n = len(s)
    if n == 0 or k > n or k <= 0:
        return ''
    return sorted([''.join(s[i:i+k]) for i in range(0, n-k+1)], key=len, reverse=True)[0]

# using zip(*args, key=len)
# here they are concatenating with an empty string for the condition returns of an empty string
def longest_consec(strarr, k):
    return max([''.join(tuple) for tuple in zip(*[strarr[i:] for i in range(k)])] + [''], key=len)

# here they are using list(map(len, input array)) to create an array of lengths of elements
def longest_consec(strarr, k):
    # Make sure that k is greater than zero and less that the
    # length of the array of strings. Otherwise return an empty string
    if k <= 0 or k > len(strarr):
        return ''

    # Finding the longest string consisting of k consecutive
    # strings is equivalent to finding the maximum sum of
    # k consecutive elements of an array that represents the
    # lengths of an array of strings.

    # star_lengths represents a list of lengths of the initial
    # array of strings.
    starr_lengths = list(map(len, strarr))
    # Find the maximum sum of k consecutive elements
    # requires keeping a temperary maximum length.
    temp_max_len = 0
    # We also need to keep the position of the first element of
    # each group.
    position = 0

    # Scan the whole list of lengths except the final k elements
    for p in range(len(starr_lengths) - (k - 1)):
        # We need to find the sum of the current set of elements
        # starting at position p
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p+i]
        
        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position+k]])

# nested for loop
# the internal for loop logic is reassigning array a with concatenated values 
def longest_consec(a, k):
	if len(a) == 0 or k > len(a) or k <= 0: return ''
	res=[]
	for n in range(len(a)-k+1):
		for t in range(1,k):
			a[n]+=a[n+t]
	return max(a,key=len)