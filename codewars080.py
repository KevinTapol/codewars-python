# List Filtering
# Parameters or Edge Cases:
    # inputs will be a list of non negative integers and strings
    # can the input be empty?
    # can the integers be so large that a for loop will time them out?
# Return:
    # a new list with the strings filtered out
# Examples:
    # [1,2,'a','b'] => [1,2]
    # [1,'a','b',0,15] => [1,0,15]
    # [1,2,'aasf','1','123',123] => [1,2,123]
# Pseudo Code:
    # declare an empty list
    # for each element in input list if the element is an integer then append it to the declared list
    # return the new list

# my answer
def filter_list(l):
    x =[]
    for e in l:
        if type(e) != str:
            x.append(e)
    return x 

# my answer refactored implicit return creating a new list filtering elements 
filter_list = lambda x :list(filter(lambda e: type(e) != str, x))

print(filter_list([1,2,'a','b'])) # [1,2]
print(filter_list([1,'a','b',0,15])) # [1,0,15]
print(filter_list([1,2,'aasf','1','123',123])) # [1,2,123]

# best practices and most clever
# similar to my refactored answer but using isinstance(element, str) instead of type()
def filter_list(l):
  return [i for i in l if not isinstance(i, str)]

# same answer but using type(element) instead of isinstance(element, str)
def filter_list(l):
  return [x for x in l if type(x) is not str]

# taking only elements that are integers instead of elements that are not equal to strings in type
def filter_list(l):
  return [e for e in l if type(e) is int]

# clever using product of element and 0 equal to 0
def filter_list(l):  
  return [i for i in l if i*0==0] 

# implicit return new list of elements in list if elements are integers
filter_list = lambda l: [e for e in l if isinstance(e, int)]

# using type(1) to compare as integer for elements
filter_list = lambda a : [i for i in a if type(i) == type(1)]

# recursive calling the function inside itself removing 1 element at a time if the element is s string
def filter_list(l):
  for i in l:
      if i == str(i):
          l.remove(i)
          filter_list(l)
  return l

# try except
def filter_list(l):
    try:
        return [i for i in l if isinstance(i,int)]
    except:
        return 'Error'
    
# importing pandas to analyze data
# .Series() one-dimensional array holding data of any type
# transform() method allows you to execute a function for each value of the DataFrame.
import pandas as pd
def filter_list(l):
    s = pd.Series(l)
    return s[s.transform(type)!=str].tolist()