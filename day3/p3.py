s1=[1,2,3,[1,2]]
s2=[]
#s3=s1.pop()


for i in s1:
    if type(i)==int:
        s2.append(i)
    else:
        s2.extend(i)
print(s2)