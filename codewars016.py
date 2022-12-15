"""
Function 1-hello world
Parameters or Edge Cases:
    function name must be greet
Return:
    a string hello world
Examples:
    @test.describe("Greet function")
    def _():
        @test.it("Making sure greet exists")
        def _():
            try:
                test.expect(greet)
            except NameError:
                test.fail("Greet doesn't exist")
        @test.it("Testing that it returns hello world!")
        def _():
            test.assert_equals(greet(), "hello world!", "Greet doesn't return hello world!")
Psuedo Code:
    create a function that when called returns "hello world!"
"""

# my answer and best practices
def greet():
    return "hello world!"

# my answer refactored to lambda and most clever
greet = lambda: "hello world!"

# using %s
def greet():
    return "he%sworld!" %("llo ")

# using char to return hello world!
def greet():
    charList = [104, 101, 108,108,111,32, 119,111,114,108,100,33]
    word = ""
    for char in charList:
        word += chr(char)
    return word

# using character codes to return hello world!
def greet():
    return "\u0068\u0065\u006C\u006C\u006F\u0020\u0077\u006F\u0072\u006C\u0064\u0021"

# lol string reverse
def greet():
    return '!dlrow olleh'[::-1]

# most other answers included funny if statments or ascii art my favorite being a christmas tree given it is the season
def greet():
    '''
'　　＊'　　'　★'　　＊'　　'　 ￼
＊　.　 * .'　＊＊　　'＊　　　*
＊　　.　'　　+:..:+ 　　'　 ' 　＊
.　　　＊　　☆☆☆　＊　　　.
　　*　　'　+:...+....:+　　＊
'　　　　'　☆☆☆☆☆　　　＊　'　　
　＊　* '　+:...:+＠+:...:+ 　　　'　　*
＊　.　　.☆☆☆☆☆☆☆ ＊　'　*　.
　　.　　+:..:+&+:...:+:...:+
　*　.　☆☆☆☆☆☆☆☆☆　＊　'　　　*
　.　　+:...:+♡+:...:+§+:..:+
.　*　☆☆☆☆☆☆☆☆☆☆☆　　'　*
　　.+:..:+♡+:..:+@+:..:+♡+:..:+
　.　　　　　.　▨ 　 '　' ＊　　　　　*
　　　.　*　　　　　　.　　　.　　'''
    return 'hello world!'