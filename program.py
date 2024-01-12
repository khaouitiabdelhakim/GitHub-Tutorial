def add(*args):
    return sum(args)

a, b, c = 1, 2, 3

#trying the function with 2 args
result1 = add(a, b)
print(result1)
#output: 3

#trying the function with 3 args
result2 = add(a, b, c)
print(result2)
#output: 6
