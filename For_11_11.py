

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for bb in numbers:
    if bb == 1:
        continue

    is_prime = True
    for i in range(2, bb):
        if bb % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(bb)
    else:
        not_primes.append(bb)
print('Primes: ', primes)
print('Not Primes: ', not_primes)