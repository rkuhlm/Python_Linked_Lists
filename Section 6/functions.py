def is_palindrome(string):
    return string[::-1] == string


# Will return True or False if the string is a palindrome

word = input("Enter a word: ")


if is_palindrome(word.casefold()):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))