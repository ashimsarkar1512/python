f= open("demo.txt", "r")
data=f.read()
print(data)
print(type(data))
f.close()



another=open("text.txt","r")


line2=another.read()
print(line2)


line1=another.readline()

print(line1)