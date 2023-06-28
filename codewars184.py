# Money, Money, Money
"""
Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest

Example:

  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00


After 1st Year -->
  P = 1041.00
After 2nd Year -->
  P = 1083.86
After 3rd Year -->
  P = 1128.30
Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.
"""
# Parameters or Edge Cases:
"""
inputs will be numbers greater than or equal to 0

"""
# Return:
"""
the total years needed to achieve the input desired amount given the initial invested money, interest and tax
"""
# Examples:
"""
principal = 1000, interest = 0.05, tax = 0.18, desired = 1100
p*i - p*t*i + p = year 1 of 1041.00

    1000, 0.05, 0.18, 1100 => 3
    1000,0.01625,0.18,1200 => 14
    1000,0.05,0.18,1000 => 0
"""
# Pseudocode:
"""
    # declare an integer named year as an input and set it equal to 1
    # declare an integer result and set it equal to 0 
    # add to the principal the product of principal and interest 
    # subtract that by the product of the principal, interest and tax and 
    # declare the math results equal to a variable integer result
    # if result is greater than or equal to desired return year
    # else call the function with year +1 and the result as principal
"""

# my answer and best practices
def calculate_years(p, i, t, d,):
    # declare a in integer variable for years and set it equal to 0
    year = 0
    # while the principal is less than the desired result
    while p < d:
        # set principal equal to the current principal plus the product of current principal and interest minus the product of principal, interest and tax
        p = p + p*i - p*i*t
        # add 1 to year
        year += 1
    # outside the while loop return year
    return year

# most clever
# ceil() rounds up to nearest integer
# float() converts the specified value into a floating point number
# log(x,base) returns the natural logarithm of a number, or the logarithm of number to base
# here x would be the desired var converted to a float
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0
    
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))

# using recursion
def calculate_years(principal, interest, tax, desired, years = 0):
    return calculate_years(principal + principal * interest * (1-tax), interest, tax, desired, years + 1) if desired > principal else years

# lambda using recursion
f=calculate_years=lambda p,i,t,d,n=0:f(p+p*i*(1-t),i,t,d,n+1)if p<d else n