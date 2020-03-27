def fibonacci(n):
    # Write your code here.
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = fibonacci(n-1)
    b = fibonacci(n-2)
    print(n-1,n-2)
    return  a+b

if __name__ == "__main__":

    fibonacci(5)

