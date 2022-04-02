#create *single tuple cant be created ..to create  single tuple add coma 
T1=(1,0,2,3) #homo
T2=('hello',1,2,2,3,True) #hetero
T3=()# empty
T4=(1,2,3,(2,3))# 2D
T5=(5,)# single charecter tuple
T6=tuple('goa')
# edit
#T1[0]=100 #tuple are immutable

# access add 
# delete 
#print(T1.clear())
# ops 
for i in T2:
    print(i)
# func

print(T4.sorted())


# TUPPLE IS A READ ONLY DATA TYPE WHERE AS LIAT ARE READ-WRITE DATA TYPE