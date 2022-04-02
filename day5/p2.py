
def palindrom(u):
    if len(u)<=1:
        print("palindrom")
    else:
        if u[0]==u[-1]:
            palindrom(u[1:-1])
        else:
            print("palindrom")


palindrom("radar")