# Cryptopangrams

def gcd(m, n):
    while n != 0:
        m, n = n, m%n
    return m

T = int(input())

for t in range(1,T+1):
    N, L = (int(x) for x in input().strip().split(" "))
    prods = [int(x) for x in input().strip().split(" ")]

    gcds = set(gcd(m,n) for m in prods for n in prods if m!=n and gcd(m,n)!=1)
    primes = set()

    for prime in gcds:
        primes.add(prime)
        for prod in prods:
            if prod % prime == 0:
                primes.add(prod // prime)

    mapping = {
        prime: chr(ord('A') + i)
        for i, prime in enumerate(list(sorted(list(set(primes)))))
    }

    for prime in primes:
        if prods[0] % prime == 0:
            result = [prime]
            for i in range(len(prods)):
                if prods[i] % result[i] != 0:
                    break
                if prods[i] // result[i] not in primes:
                    break
                result.append(prods[i] // result[i])

            if len(result) == L+1:
                print("Case #{}: {}".format(t, ''.join(mapping[prime] for prime in result)))
                break

'''
Note:
- Pangram: phrase that use each letter of english at least once
- Encryption scheme: 
    - choose 26 different prime numbers smaller than N
    - Sort primes in increasing order and assign in order of A, B, C, ...
    - Message sent in order of P1*P2, P2*P3, P3*P4, ..., PN-1*PN

Test Case:
1: 103(max prime), 31(message length), 217 1891 ... => CJQUIZ...

Limitations:
Tests = 1-100
Memory = 1GB
L (message length) = 25-100
T1: 101 < N < 10000
T2: 101 < N < 10^100

Solution:
- Semi prime factorization: http://www2.mae.ufl.edu/~uhk/QUICK-SEMI-PRIME-FACTORING.pdf
-> use euclidean algorithm (greatest common divisor)
'''
