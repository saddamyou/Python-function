def string(str1):
     x  = ''
     index = len(str1)
     while index > 0:
          x = x + str1[index - 1]
          index = index - 1
     return x
print(string('1234abcd'))