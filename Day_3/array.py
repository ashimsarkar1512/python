marks=[12,13,14,15,16,20]
print(marks)
print(type(marks))

list=[1,2,3,4,5,6,7]
print(list)
list.append(9)
print(list)


# sorting in list number and string

number=[1,2,3,9,4,5,6,7]

number.sort()
print(number)

number.sort(reverse=True)
print(number)



# string value sort korte tar first letter er upor depend korte hoi

stringList=["ashim","sagor","mohadev","laboni","juthi"]


stringList.sort()
print(stringList)

stringList.sort(reverse=True)
print(stringList)


letter=["a","b","c","d","e"]
letter.sort()
print(letter)
letter.reverse()
print(letter)

letter.sort(reverse=True)
print(letter)

letter.insert(1,"k")
print(letter)

letter.append("As")
print(letter)


stringList.remove("ashim")
print(stringList)

number.pop(4)
print(number)

