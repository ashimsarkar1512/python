# normal way
movie1=input("enter your favourite movie1:")
movie2=input("enter your favourite movie2:")
movie3=input("enter your favourite movie3:")

list=[movie1,movie2,movie3]
print(list)


# best way

movies=[]
mov1=input("enter your favourite mov1:")
mov2=input("enter your favourite mov2:")
mov3=input("enter your favourite mov3:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# best way


cinema=[]

cinema.append(input("enter your favourite movie one:"))
cinema.append(input("enter your favourite movie two:"))
cinema.append(input("enter your favourite movie three:"))

print(cinema)



# Palindrom

list=[1,2,3]

copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
    print("palindrom")  
else:
    print("Not palindrom")          
countStr=["A","B","C","A","B","A"]
grade=countStr.count("A")
print(grade)


countStr.sort()

