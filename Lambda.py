# # # def apply(criteria , n):
# # #      count = 0
# # #      for i in range(n + 1):
# # #           if criteria(i):
# # #                count += 1
# # #      return count
# # # def is_even(x):
# # #      return x%2 == 0
# # # print(apply(is_even, 10))

# # # def apply(criteria, n):
# # #     count = 0
# # #     for i in range(n + 1):
# # #         if criteria(i):
# # #             count += 1
# # #     return count
# # #
# # #
# # # def is_even(x):
# # #     return x % 2 == 0
# # #
# # #
# # # print(apply(is_even, 10))

# # def sum_odd(a, b):
# #     sum_of_odds = 0
# #     for i in range(a, b + 1):
# #         if i % 2 == 1:
# #             sum_of_odds += 1
# #     return sum_of_odds


# # low = 2
# # high = 7
# # my_sum = sum_odd(low, high)











# def apply(criteria, n):
#     count = 0
#     for i in range(n+1):
#         if criteria(i):  # is a boolean
#             count += 1
#     return count


# def is_even(x):
#     return x % 2 == 0


# how_many = apply(is_even, 10)
# print(how_many)



def remove_all(l, e):
    #make a copy
    lnew = l[:]
    # clear the list
    l.clear()  # l becomes []
    # add back element that do not equal e
    for n in lnew:
        if e != n:
            l.append(n)


lin = [1, 2, 2, 2]
remove_all(lin, 2)
print(lin)
lin = [1, 2, 2, 2]
remove_all(lin, 1)
print(lin)
lin = [1, 2, 2, 2]
remove_all(lin, 0)
print(lin)
