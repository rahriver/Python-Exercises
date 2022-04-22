def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime =  False
    return prime

primes = []

for i in range(1,1001):
    print(i,is_prime(i))
    if is_prime(i) == True:
        primes.append(i)
print(primes)
print(len(primes))
