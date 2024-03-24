def pas(n):
    if n <= 1:
        return n 
    else:
        return 2**n+pas(2**(n-1))
       
       
n=int(input("enter row: "))
print(pas(n))
