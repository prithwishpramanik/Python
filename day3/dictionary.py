# mutable        non mutable
# list,set,dict  int,float,boolean


#dictonary 
    # keys->immutable 
    # keys cant repeat no indexing

d1={'name':'prithwish','age':21,'marks':{
    'os':21,
    'ds':32,
    'math':85
}}

print(d1['marks']['math'])


#edit
d1['marks']['math']=60
print(d1)

#add
d1['college']='HIT'
print(d1)

d1['marks']['eng']=60
print(d1)

#del

del d1['marks']['eng']
print(d1)

for i in d1:
    print(i,d1[i])

#dic is all about keys

#function
d1.keys()
d1.values()