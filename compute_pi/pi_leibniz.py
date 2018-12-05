
# Gregory-Leibniz series
PI = 0
n = 0
while True:
    if n % 2 == 0:
        PI += 4/(2 * n + 1)
    else:
        PI -= 4/(2 * n + 1)
    n+=1

    if n == 1000000:
        print("n times: " + str(n))
        print("pi is: " + str(PI))
