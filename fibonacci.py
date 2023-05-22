import sys
print(sys.getrecursionlimit())

# Fibonacci function
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)


# Solution 1
# Introduce recursion in programing   https://www.youtube.com/watch?v=ixdr6V2vRC4
# This solution won't work for large number due to the expensiveness of recursion
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(20))


# Introduce dictionary in python 
# https://www.youtube.com/watch?v=rZjhId0VkuY 
# https://www.youtube.com/watch?v=daefaLgNkw0
# This one still uses recursion, but dramatically improves performance by only calculate each fibonacci number once
fibonacci_dic = {0: 0, 1: 1}
def fibonacci_improved(n):
    if fibonacci_dic.get(n) is not None:
        return fibonacci_dic.get(n)
    else:
        result = fibonacci_improved(n-1) + fibonacci_improved(n-2)
        fibonacci_dic[n] = result
        return result

print(fibonacci_improved(30))
