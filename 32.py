def fibonacci(n):
    if n <= 0:
        return "n ədədi 1-dən böyük olmalıdır!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("n-ci həddi daxil edin: "))
result = fibonacci(n)
print(f"{n}-ci Fibbonaççi həddi: {result}")