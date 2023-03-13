# Descending Order
# Parameters or Edge Cases:
    # inputs will be non negative integers
# Return:
    # rearrange the digits to create the highest possible number
# Examples:
    # 42145 => 54421
    # 145263 => 654321
    # 123456789 => 987654321
# Pseudo Code:
    # convert the input to a string then to an array
    # make a shallow copy array converting each element back into an integer
    # return the new array sorted from highest to lowest

# my answer
def descending_order(n):
    # convert the input to a string then to an array
    s = list(str(n))
    # make a shallow copy array converting each element back into an integer sort it then reverse the array
    l = sorted(map(int, s))[::-1]
    # make a shallow copy converting each string back into a string and join back with no spaces
    m = "".join(map(str, l))
    # return the string as an integer
    return int(m)

# my answer refactored implicit return
descending_order = lambda n: int("".join(map(str, sorted(map(int, list(str(n))))[::-1])))

print(descending_order(42145)) # 54421
print(descending_order(145263)) # 654321
print(descending_order(123456789 )) # 987654321

# best practices and most clever
# I completely forgot sorted() has a second argument for reversing
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

# This breakdown helps to think of each step at a time
def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)

# Cleaner version of my refactored answer but not an implicit return
def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))

# testing for anything other than non negative integers
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')
    
# clean implicit return lambda
Descending_Order = lambda n: int(''.join(reversed(sorted(str(n)))))

# while loop
def Descending_Order(num):
    digits = []
    
    while num > 0:
        new_num = num // 10
        digits.append(num - new_num*10)
        num = new_num
        
    out = 0
    for i, digit in enumerate(sorted(digits)):
        out += digit * 10**i
        
    return out

# while loop with array methods
def Descending_Order(num):
    #Bust a move right here
    list=[]
    while num/10 !=0 :
        list.append(num%10)
        num=num/10
    list.append(num)
    list.sort()

    numb=0
    i=0
    
    while i <len(list):
        numb+=list[i]*pow(10,i)
        i+=1
    return numb

# I completely forgot about for each element in array. I would have used this for converting integer and string.
def Descending_Order(num):
    y=sorted([x for x in str(num)])
    y.reverse()
    return int(''.join(y))

# .sort()
def Descending_Order(num):
    x = [i for i in str(num)]
    x.sort()
    return int(''.join(x[::-1]))

# .sort() has an argument for reversed!
def Descending_Order(num):
    li=[x for x in str(num)]
    li.sort(reverse=True)
    return int(''.join(x for x in li))

# nested for element in array
def descending_order(num):
    return int(''.join([str(x) for x in sorted([int(i) for i in str(num)],reverse=True)]))

# using for elements in array to organize highest to lowest
def descending_order(num):
    digs = [0 for _ in range(10)]

    for d in str(num):
        digs[int(d)] += 1

    str_res = "0"
    for i in range(10):
        if digs[9 - i]:
            str_res += str(9 - i) * digs[9 - i]

    return int(str_res)

# nested while loop
def descending_order(num):
    
    num = str(num)
    a = []
    
    i = 10
    while 0 <= i:
        j = 0
        while j < len(num):
            if i == int(num[j]):
                a.append(str(i))
            j = j + 1
        i = i - 1
    return(int("".join(a)))