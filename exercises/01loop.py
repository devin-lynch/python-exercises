# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

# i = 0

# def p_times(statement, num):
#     global i
#     while i < num:
#         print(statement)
#         i += 1

# p_times('Hello', 3)


# CLASS REVIEW

def p_times(statement, nums):
    # # using a for loop...
    # for i in range(nums):
    #     print(statement)

    # using a while loop
    i = 0
    while i < nums:
        print(statement)
        i += 1

# p_times('Hello there', 1)
p_times('Hello there', 4)
