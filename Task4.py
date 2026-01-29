# Task: Calculator Program
# Create a Python program that acts as a basic
# calculator. It should prompt the user to
# enter two numbers and an operator (+ , -, *, /, %), and then display the result of the
# operation.


def cal():
    while True:
        user = input("Type 'yes' to exit or press Enter to continue: ").strip().lower()
        if user == "yes":
            print("EXIT FROM CALCULATOR")
            break

        n1 = int(input("ENTER THE FIRST NUMBER:")) 
        n2 = int(input("ENTER THE SECOND NUMBER:"))
        op = input("ENTER THE OPERATION TO BE PERFORMED (+, -, *, /,%): ").strip()

        if op == "+":
            print("ADDITION:", n1 + n2)
        elif op == "-":
            print("SUBTRACTION:", n1 - n2)
        elif op == "*":
            print("MULTIPLICATION:", n1 * n2)
        elif op == "/":
            print("DIVISION:", n1 / n2)

        elif(op=="%"):
            print("MODULO::",n1%n2)
        else:
            print("Invalid operation!")

cal()
