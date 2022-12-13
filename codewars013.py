"""
Parameters or Edge Cases:
    input will be a string with spaces
Return:
    the input string without the spaces
Examples:
    (no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
    (no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
    (no_space('8aaaaa dddd r     '), '8aaaaaddddr')
    (no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
    (no_space('8j aam'), '8jaam')
Psuedo Code:
    create an empty list
    for each element that is not empty append it to the empty list
    convert the list back into a string and return it
"""

# my answer
def no_space(arr):
    # create an empty list
    l = []
    # for each element that is not empty append it to the empty list
    for i in range(0,len(arr)):
        if (arr[i] != " "):
            l.append(arr[i])
    # convert the list back into a string and return it        
    return ''.join(l)

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B')) # '8j8mBliB8gimjB8B8jlB'
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd')) # '88Bifk8hB8BB8BBBB888chl8BhBfd'
print(no_space('8aaaaa dddd r     ')) # '8aaaaaddddr'
print(no_space('jfBm  gk lf8hg  88lbe8 ')) # 'jfBmgklf8hg88lbe8'
print(no_space('8j aam')) # '8jaam'

# best practices and most clever
def no_space(x):
    return x.replace(' ' ,'')

# using .join() and .split()
def no_space(x):
    return "".join(x.split())

# concatenating
def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char

# using .join() with a for loop
def no_space(x):
    return ''.join(i for i in x if i !=' ')

# using regex
import re

def no_space(x):
    return re.sub(r'\s+','',x,0)

# one liner lambda
no_space = lambda x: ''.join(x.split())

# using filter()
no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))