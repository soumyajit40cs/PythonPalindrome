def is_palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 0:
        return False
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a ='k2k'
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
