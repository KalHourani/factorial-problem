
def factorial(n, cache=[1]):
    if n < len(cache) and cache[n]:
        return cache[n]
    else:
        cache.append(n * factorial(n - 1))
        return cache[n]


def tau(n, cache=[0]):
    if n < len(cache) and cache[n]:
        return cache[n]
    else:
        i = 2 * n
        while (n ** i >= factorial(i)):
            i += 1
        cache.append(i)
        return i


def main():
    i = 1
    while True:
        print(i, tau(i) / i)
        i += 1
    return 0

if __name__ == "__main__":
    main()