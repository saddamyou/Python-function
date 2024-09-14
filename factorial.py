# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#        return  n * factorial(n -1)
# n = int(input("Enter the number of n "))
# print(factorial(n))
        

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
num = 5
result = factorial(num)
print("The value of the factorial is: ", result)
    
        
