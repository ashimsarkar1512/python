collection ={1,2,2,2,3,3,4,5,"hello","prity"}

print(type(collection))
print(len(collection))

collection.add(9)
print(collection)

collection.add(("ashim",1,3))
print(collection)
collection.remove(3)
print(collection)

collection.clear()
print(collection)


collectionData={"prity","mukti","mritra","dighi","ashim"}
collectionData.pop()
print(collectionData)

set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(set1.union(set2))
print(set1.intersection(set2))