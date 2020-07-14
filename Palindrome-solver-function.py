#**Check if Palindrome** - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

def check_palindrome(string):
    return string[::] == string[::-1] 