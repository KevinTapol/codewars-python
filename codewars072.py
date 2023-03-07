# Beginner Series #4 Cockroach
# Parameters or Edge Cases:
    # inputs will be numbers and can be floats representing km per hour
# Return:
    # the input as cm per second rounded down to the nearest integer floored
# Examples:
    # 1.08 --> 30
    # 1.09 --> 30
    # 0 --> 0

# Pseudo Code:
    # to convert km/h to cm/s divide the input by 0.036
    # then round down or take the integer from the quotient

# my answer
def cockroach_speed(s):
    return int(s//0.036) or 0

# my answer refactored implicit return
cockroach_speed = lambda s: int(s//0.036) or 0
# fyi the kata accepted which allows division by 0 and the return of float
cockroach_speed = lambda s: s//0.036

print(cockroach_speed(1.08)) # 30
print(cockroach_speed(1.09)) # 30
print(cockroach_speed(0)) # 0

# best practices and most clever
# this is dividing by 0 and returning floats which goes against the return request being integers
def cockroach_speed(s):
    return s // 0.036

# breaking down the math conversions instead of using fractions
def cockroach_speed(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)

# same idea as above multiply by 100000 for cm  then dividing by 60*60 to convert to hours to seconds
def cockroach_speed(s):
    return (s * 100000) // (60 * 60) 

# importing math to use math.floor()
import math
def cockroach_speed(s):
    return math.floor(s * 27.778)

# multiplying by 27.7778 and using int() instead of dividing by 0.036
def cockroach_speed(s):
    return int(s * 27.7778)

# declaring variables for conversions
ONE_KM_IN_METERS = 1000
ONE_METER_IN_CM = 100
ONE_HOUR_IN_MINUTES = 60
ONE_MINUTE_IN_SECONDS = 60

def cockroach_speed(s):
    cm = ONE_KM_IN_METERS * ONE_METER_IN_CM
    sec = ONE_HOUR_IN_MINUTES * ONE_MINUTE_IN_SECONDS
    return int((s * cm) / sec)

# clever using // to divide by one and take only the integer
cockroach_speed = lambda s: s * 27.778 // 1

# including import in the lambda
cockroach_speed = lambda s: __import__('math').floor(s*1000*100/60/60)