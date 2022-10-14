# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

# number_list = [1, 2, 3]
# new_list2 = []

# def multiply_by(num_list, num):
#     for number in num_list:
#         number *= num

# multiply_by(number_list, 5)

# new_list = [5*i for i in number_list]
# print(new_list)


# CLASS REVIEW



def multiply_by(li, num):
    # # iterate the list in a way that allows us to mutate the list
    ## enumerate
    # for i, list_num in enumerate(li):
    #     li[i] = list_num * num

    # range
    for i in range(len(li)):
        li[i] *= num

    return li

print(multiply_by([1, 2, 3], 5))

