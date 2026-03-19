import time

def run(limit=500000):
    start = time.time()
    primes = []

    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    duration = time.time() - start
    return {
        "duration": round(duration, 3),
        "primes_found": len(primes)
    }