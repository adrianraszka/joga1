#TODO: Find the sum of all the multiples of 3 or 5 below 1000.

# def m3o5(limit):
#     sum = 0
#     for i in range(limit):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     print(sum)
#
# m3o5(1000)

#TODO: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#
# def fibo_even(limit):
#     sum = 0
#     a, b = 1, 2
#     while a < limit:
#         a, b = b, a + b
#         if a % 2 == 0:
#             sum += a
#     print(sum)
# fibo_even(4e6)

#TODO: What is the largest prime factor of the number 600851475143 ?

# def lp(limit):
#     for i in range(1, limit):
#         if limit % i == 0:
#             limit /= i
#             print(limit, i)
#
# lp(600851475143)

#TODO: Find the largest palindrome made from the product of two 3-digit numbers.

# def pali(limit_up, limit_down):
#     pals = []
#     for i in range(limit_up, limit_down, -1):
#         for j in range(limit_up, limit_down, -1):
#             sum = i * j
#             L = list(map(int, str(sum)))
#             if L == L[::-1]:
#                 pals.append(sum)
#     print(max(pals))
#
# pali(1000, 100)

#TODO: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# from math import gcd
#
# lcd = 1
# for i in range(20):
#     lcd *= (i + 1) // gcd(lcd, i + 1)
# print(lcd)

#TODO: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# def sum(limit):
#     sum_sq = 0
#     for i in range(1, limit + 1):
#         sum_sq += i**2
#     print(sum_sq)
#
#     sum_sum = 0
#     for j in range(1, limit + 1):
#         sum_sum += j
#         sum_sum2 = sum_sum**2
#     print(sum_sum2)
#
#     print(sum_sum2 - sum_sq)
# sum(100)

#TODO: What is the 10001st prime number? (thanks stackoverflow)


# primez = []
# i = 1
# j = 4
# while 0 == 0:
#     i += 1
# sieve becomes useless for large numbers
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0:
#         j += 1
#         print(j, i)
#         if i == 104743:
#             break;


def is_prime(n):
    if n < 2:
        return False
    i = 3
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 2
    return True

def n_prime(n):
    i = 3
    while n > 0:
        if is_prime(i):
            n -= 1
            if n == 0:
                return i
        i += 2

print(n_prime(10001 -1))









