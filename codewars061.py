# Grasshopper - Grade book
# Parameters:
    # inputs will be 3 integers 0-100 inclusively 
# Return:
# the average of the integers as a letter grade value

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'

# Examples:
    # (95, 90, 93) => 'A'
    # (70, 70, 100) => 'B'
    # (70, 70, 70) => 'C'
    # (65, 70, 59) => 'D'
    # (44, 55, 52) => 'F'
# Pseudo Code:
    # add up the three inputs and divide by 3
    # if the quotient is inclusively between 90 and 100 return string 'A'
    # if the quotient is less than 90 but more than or equal to 80 return string 'B'
    # if the quotient is less than 80 but more than or equal to 70 return string 'C'
    # if the quotient is less than 70 but more than or equal to 60 return string 'D'
    # else return string 'F'

# my answer
def get_grade(s1, s2, s3):
    # add up the three inputs and divide by 3
    q = (s1 + s2 + s3)/3
    # if the quotient is inclusively between 90 and 100 return string 'A'
    if 90 <= q <= 100:
        return 'A'
    # if the quotient is less than 90 but more than or equal to 80 return string 'B'
    elif q >= 80:
        return 'B'
    # if the quotient is less than 80 but more than or equal to 70 return string 'C'
    elif q >= 70:
        return 'C'
    # if the quotient is less than 70 but more than or equal to 60 return string 'D'
    elif q >= 60:
        return 'D'
    # else return string 'F'
    else:
        return 'F'
    
# my answer refactored lambda implicit return nested conditionals
get_grade = lambda s1, s2, s3,: 'A' if (s1 + s2 + s3)/3 >= 90 else 'B' if (s1 + s2 + s3)/3 >= 80 else 'C' if (s1 + s2 + s3)/3 >= 70 else 'D' if (s1 + s2 + s3)/3 >= 60 else 'F' 
    
print(get_grade(95, 90, 93)) # 'A'
print(get_grade(70, 70, 100)) # 'B'
print(get_grade(70, 70, 70)) # 'C'
print(get_grade(65, 70, 59)) # 'D'
print(get_grade(44, 55, 52)) # 'F'


# best practices 
# the only difference from mine is they divided by a float
def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"

# using dictionary key value and .get(math eval for key call, or 'F')
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

# using // to divide an only return the solid integer for index location call
def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]


# very clever sum() can only take 2 inputs here they are using an array so technically 1 input instead of 3
def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'

# using *args to sum all the inputs like spread in JS (...inputs)
scores = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

def get_grade(*args):
    mean = sum(args) / len(args)
    return scores.get(mean // 10, 'F') 

# using *args but lambda implicit one liner string index call on sum math eval
get_grade = lambda *a: "FFFFFFDCBAA"[(sum(a)//3)//10]

# using for element in array
def get_grade(*grades):
    mean = sum(grades)/len(grades)
    for score, grade in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]:
        if mean >= score:
            return grade
        
# using max(int(sum(input)/30-5), 0) with *args for spread
def get_grade(*arg):
    return list('FDCBAA')[max(int(sum(arg)/30-5), 0)]

# using enumerate()
def get_grade(s1, s2, s3):
  return next('ABCDF'[i] for i, low in enumerate([90, 80, 70, 60, 0]) if (s1+s2+s3) / 3 >= low)