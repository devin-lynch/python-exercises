# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#


def factorial(n):
    whole_number = 1
    i = 0
    while i < n:
        i += 1
        whole_number *= i
    print(whole_number)

factorial(5)

