#sets are mutable 
# sets cant have mutable data types (multi sets  cant happen)
# sets cant have duplicate 
# no indexing and slicing


#create 
s1={1,2,3}
s2={'helo',1,2,30}
s3=set() #empty set
s4={1,2,5,2,4,3} #no duplicate allowed
print(s4)
# acess edit cant be done as indexing not possible
#  add 

print(s1.add(5))
# delete
del s1
#print(s1.pop()) #del first item
#  op
print(s1|s2)#union
print(s1&s2)#
print(s1-s2)
print(s1+s2)


#  func

print(s1.isdisjoint(s2))