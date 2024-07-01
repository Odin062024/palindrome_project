a_string = 'potop'

def palindrome(a_string):
    a_string = a_string.lower()
    return a_string == a_string[::-1]