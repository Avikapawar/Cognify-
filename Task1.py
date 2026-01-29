
# Task: String Reversal
# Create a Python function that takes a
# string as input and returns the reverse of
# that string. For example, if the input is
# "hello,
# " the function should return
# "olleh."
def string_reverse(text):
    return text[::-1]

text=input("Enter the String::")
reverse=string_reverse(text)
print(f"Reverse of {text} is::",reverse)  