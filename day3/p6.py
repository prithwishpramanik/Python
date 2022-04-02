song=input("enter song name :")

song2=list(song.split())
song1=tuple(song2)
print(song1)
 #list er athe compare korte ghobe
for j in range(len(song2)):
    counter=0
    sang=song2.pop()
    
    for i in song1:
        
        if(i == sang):
            counter=counter+1
            print(max(i))
            print(counter)
            
         
        
