#TODO: Find the sum of all the multiples of 3 or 5 below 1000.

# def m3o5(limit):
#     sum = 0
#     for i in range(limit):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#             print(sum)
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

def pali(limit_up, limit_down):
    pals = []
    for i in range(limit_up, limit_down, -1):
        for j in range(limit_up, limit_down, -1):
            sum = i * j
            L = list(map(int, str(sum)))
            if L == L[::-1]:
                pals.append(sum)
    print(max(pals))

pali(1000, 100)




















