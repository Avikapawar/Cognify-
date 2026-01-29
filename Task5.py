# Task: Palindrome Checker
# Write a Python function that checks whether
# a given string is a palindrome. A palindrome
# is a word, phrase, or sequence that reads the
# same backward as forward (e.g.,"madam" or "racecar").
def string_reverse(text):
    word=text[::-1]
    if word==text:
        print("IS PALINDROME:",text) 
    else:
        print("IS NOT PALINDROME:",text)

text=input("Enter the String::")
reverse=string_reverse(text)
