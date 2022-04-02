def multiply(a):
    if a==1:
        return 1
    else:
        return a*multiply(a-1)

print(multiply(5))