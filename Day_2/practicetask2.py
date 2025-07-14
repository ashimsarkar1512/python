name=input("enter your name:")


print("name lenth:",len(name))


dollarCount="$i am a $ student in $ northern university"
print(dollarCount.count("$"))

print(dollarCount.find("am"))

print(dollarCount.replace("i","he"))





number=int(input("enter your number: "))
remainder=number%2
if(remainder==0):
    print("this is even number")
else:
    print("this a odd number")    


a=7
b=40
c=20


if(a>=b and a>=c):
    print("a is grater than b,c")
elif(b>=c):
    print("b is grater than a,c")  
else:     
    print("c is grater than a,b")    


A=int(input("enter your first number: "))
B=int(input("enter your second number: "))
C=int(input("enter your third number: "))

if(A>=B and A>=C):
    print("A is Largest number")
elif(B>=A and B>=C):
    print("B is largest number")   
else:
    print("C is largest number")     


num1=int(input("enter your num1 :"))
num2=int(input("enter your num2 :"))
num3=int(input("enter your num3 :"))
num4=int(input("enter your num4 :"))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print("num1 is largest number")
elif(num2>=num1 and num2>=num3 and num2>=num4):
    print("num2 is largest number")    
elif(num3>=num1 and num3>=num2 and num3>=num4):
    print("num3 is largest number")    
else:
    print("num4 is largest number")



numberis=int(input("enter your multiple number :"))
multiple=numberis%7


if (multiple==0):
    print("this number is multiple 7")
else:
    print("this is not multiple 7")    