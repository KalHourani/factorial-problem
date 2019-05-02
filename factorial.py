#!/usr/bin/python3

from math import factorial

def tau(n, cache={}):
    if n in cache:
        return cache[n]
    else:
        i = 2 * n
        while (n ** i < factorial(i)):
            i += 1
        cache[n] = i
        return i

def main():
    for i in range(1, 1000):
        print(i, tau(i))
    return 0

if __name__ == "__main__":
    main()