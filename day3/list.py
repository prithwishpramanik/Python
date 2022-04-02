l1=[1,23] #homogenous list not present in array...list are mutable
l2=['hello',123,True] #heterogeniois list not present in array
l3=[]#empty list
l4=[1,2,3,[1,2]] #2d list 
l7=[[[1,2],[3,4]],[[5,4],[7,8]]]
l6=l4[-1][-1]
l5=list('goa')
print(l6)
print(l7)
l8=l7[-1][-2][-1]
print(l8)

#append
l10=l5.append('hello')
l9=l1.append(100)
print(l5)

#extend
l1.extend([100,200])
print(l1)

#
l1.extend('goa')

l1.insert(1,50)

#del
del l1[::2]

l2.remove('hello')#for deleting the element whose postion is not known

l1.pop()#last item is deleted
print(l1)
l1.pop(0)#element in ondex position

l1.clear()
print(l1)



