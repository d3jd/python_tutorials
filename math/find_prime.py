def isPrime(n):
    for i in range(3, n):
        if n % i == 0:
            print(str(n) + " is not prime")
            print(str(n) + " is divisible by " + str(i))
            return False
    print(str(n) + " is prime!")
    return True

x = 3
while x < 10:
    isPrime(x)
    x+=1
