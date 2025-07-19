def multiple(a,b,c):
    multi=(a*b*c)
    return(multi)

solve=multiple(2,3,4)
print(solve)



def ageEquation(a,b,c):
    if(a>=b and a>=c):
        return ("a is a big brother")
    elif(b>=c and b>=a):
        return("b is a big brrother")
    else:
       return ("c is a big brother")
    

result=ageEquation(7,9,8)

print(result)
