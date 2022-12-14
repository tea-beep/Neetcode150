#test cases

#functions 
#************** EASY #**************
def isPalindrome(s):

#** this solution works but uses built in functions and add'l memory since it creates new strings.**
#     newStr = ""
#     # build new string of just alpha-numeric characters from input
#     for c in s:
#         if c.isalnum():
#             #if it is alnum then add to the string.
#             newStr += c.lower()
#     #check if the string equals its reverse.
#     if newStr == newStr[::-1]:
#         return True
#     return False
#******************************************************************************

#convert all uppercase to lowercase, remove all non-alphanumeric, check front to back
    newStr = ""

    s = s.lower()
    for char in s:
        if char.isalnum() == True:
            newStr += char
    return newStr == newStr[::-1]
    
#this solution uses pointers to check from the l and r that the characters are equal. When the pointers pass or meet we
#stop
#     l, r = 0, len(s) -1
#     while l < r:
#         while l < r and not self.alphaNum(s[l]):
#             l += 1
#         while r > l and not self.alphaNum(s[r]):
#             r -= 1
#         if s[l].lower() != s[r].lower():
#             return False
#         l += 1
#         r -= 1
#     return True


# #define alphanum function to determine if a character is alphanumerical.
# def alphaNum(self, c):
#    return (ord('A')<= ord(c) <= ord('Z') or
#            ord('a')<= ord(c) <= ord('z') or
#            ord('0')<= ord(c) <= ord('9'))


#print statements/tests