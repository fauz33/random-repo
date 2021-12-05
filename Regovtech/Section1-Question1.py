def my_factorial(x):
    if x !=1:
        return x * my_factorial(x-1)
    else:
        return 1

def my_sum(x):
    total_no=0
    for i in str(x):
        total_no+=int(i)
    return total_no

print(my_sum(my_factorial(100)))
