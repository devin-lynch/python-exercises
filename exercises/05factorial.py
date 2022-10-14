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


# def factorial(n):
#     whole_number = 1
#     i = 0
#     while i < n:
#         i += 1
#         whole_number *= i
#     print(whole_number)

# factorial(5)


# CLASS REVIEW

print(range(1, 10))

def factorial(num):
    # keep track of factorial
    # prod = 1
    # # loop up to the num and multiply the product by each number
    # for i in range(1, num):
    #     prod *= i

    if num < 3:
        return num

    # recursive case
    return num * factorial(num - 1)

    return prod

print(factorial(5))
