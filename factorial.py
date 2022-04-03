def factorial(n):
    index = n-1
    while index >= 1 :
        n = n * index
        index -= 1
           
    return n

n = 5
result = factorial(n)
print("factorial of " + str(n) + " is " + str(result))
    
    