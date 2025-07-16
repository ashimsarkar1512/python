info={
    "name":"Ashim",
    "subject":["python","C","javascript"],
    "Touple":("anik","ayon"),
    "marks":98.7,
    "age":23,
    "is_adult":True
}
print(info)

print(info["name"])

info["name"]="prity"
print(info)


name={}

name["firstname"]="Ashim"
name["surname"]="kumar"
name["age"]=23
name["education"]="bsc in cse"
name["department"]="computer science and engineering"
print(name)


studentName={
    "name":"ashim kumar sarkar",
    "marks":{
        "phy":80,
        "chemistry":89.5,
        "bangla":100,
    }
}

print(studentName)


print(studentName["marks"]["phy"])

print(len(list(studentName.values())))

print(studentName.items())

pairs=list(studentName.items())

print(pairs[1])

getdata=studentName.get("name")
print(getdata)

new_data={"name":"prity","age":23}


studentName.update(new_data)

print(studentName)


