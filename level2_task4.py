#Task: Fibonacci Sequence
#Write a Python function that generates the
#Fibonacci sequence up to a given number of
#terms. The function should take an integer
#input from the user and display the
#Fibonacci sequence up to that number of terms.

def fibonacci(n):
    a, b = 0, 1
    
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Enter the number of terms: "))
fibonacci(terms)
