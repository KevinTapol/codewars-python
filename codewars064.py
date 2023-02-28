# Third Angle of a Triangle
# Parameters or Edge Cases:
    # inputs will be 2 integers greater than 0 representing 2 angles of a triangle
# Return:
    # the 3rd angle by subtracting 180 by the inputs
# Examples:
    # (30, 60) => 90
    # (60, 60) => 60
    # (43, 78) => 59
    # (10, 20) => 150
# Pseudo Code:
    # return the result of 180 - inputs
# my answer
def other_angle(a, b):
    return 180 - (a + b)

# my answer refactored implicit lambda
other_angle = lambda a,b: 180 - (a + b)

print(other_angle(30, 60)) # 90
print(other_angle(60, 60)) # 60
print(other_angle(43, 78)) # 59
print(other_angle(10, 20)) # 150

# best practices and most clever
def other_angle(a,b):
    return 180 - a - b

# using sum
def other_angle(*a):
    return 180 - sum(a)

# dictionary/object index call
def other_angle(a, b):
    return {True: 180-a-b, False: 'not possible'}[a+b <= 180 and a > 0 and b > 0]