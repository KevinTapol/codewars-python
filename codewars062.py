# Area or Perimeter
# Parameters or Edge Cases:
    # inputs will be 2 integers representing length and width
    # inputs will be integers greater than 0
# Return:
    # if inputs equal return the product of the inputs
    # if the inputs are not equal add the inputs together and multiply by 2 return the product
# Examples:
    # 6, 10 --> 32
    # 3, 3 --> 9
# Pseudo Code:
    # if both inputs are equal return the product of the inputs
    # else return the product of 2 * the sum of the inputs

# my answer
def area_or_perimeter(l , w):
    # if both inputs are equal return the product of the inputs
    if l == w:
        return l*w
    # else return the product of 2 * the sum of the inputs
    else:
        return 2 * (l + w)
    
# my answer refactored implicit return one liner
area_or_perimeter = lambda l, w: l*w if l==w else 2*(l+w)
    
print(area_or_perimeter(6, 10)) # 32
print(area_or_perimeter(3, 3)) # 9

# best practices and most clever was a combination of my answers
def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2

# evaluating truthy/falsy index call on an array math eval
def area_or_perimeter(l , w):
    return [(l+w)*2, l*w][(l == w)]

# same idea but reversing the index call eval
def area_or_perimeter(l , w):
    return [l*w , 2*(l + w)][l != w]

# clever imo taking an input to the power of 2 if the inputs are equal instead of multiplying by itself
area_or_perimeter = lambda _,__: _**2 if _==__ else 2*(_+__)