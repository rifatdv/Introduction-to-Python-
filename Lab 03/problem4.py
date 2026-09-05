sum = 0

for num in range(2, 1000):
    isPrime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        sum += num

print("Sum of the prime numbers below 1000 =", sum)