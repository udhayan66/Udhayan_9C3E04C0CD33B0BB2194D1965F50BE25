
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
print(format("FACTORIAL",'^60'))
n=int(input("Enter a number to find factorial:"))
print("factorial of",n,"is:",factorial(n))