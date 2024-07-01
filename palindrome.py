a_string = 'Potop'

def palindrome(a_string):
    a_string = a_string.lower()
    return a_string == a_string[::-1]

print(palindrome(a_string))