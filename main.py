def fibonacci(n):
    if n <= 0:
        return "Nah"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 9
result = fibonacci(n)
print(f"{n}th Fibonacci number: {result}")