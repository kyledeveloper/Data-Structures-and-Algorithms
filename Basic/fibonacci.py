def fibonacci1_loop(n):

    f1 = 1
    f2 = 1
    for i in range(3,n+1):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    return f2


f = fibonacci1_loop(6)
print(f)