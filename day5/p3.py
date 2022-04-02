


def power(a):
    if a==1:
        print(1)
    else:
        if (a**a)%2==0:
            print(a)
            power(a-1)
        else:
            power(a-1)
        


power(10)