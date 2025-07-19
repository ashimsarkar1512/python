heroes=["ironman","spiderman","superman","shaktiman","machineman"]
cities=["dhaka","rajshahi","khulna","chattogram","maymanshing","rangpur"]

def print_len(list):
    print(len(list))

print_len(cities)  
print_len(heroes)  



def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)  
print()



n=5
fact=1
for i in range(1,1+n):
    fact *=i
    print(fact)


def cal_fac(n):
    fact=1
    for i in range(1,1+n):
        fact *=i
        print(fact)
cal_fac(6)    




def converter(usd):
    taka=usd*122
    return(usd, "USD = " ,taka)

usd_val=converter(1)
print(usd_val)
