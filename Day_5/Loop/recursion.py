# recursiive function
def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)

# show(5)    



def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n


multi=fact(4)
print(multi)



def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n

sum=cal_sum(5)

print(sum)




def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)


fruits=["mango","banana","apple","orange"]

print_list(fruits)

