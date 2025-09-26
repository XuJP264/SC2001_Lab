def gcd(a,b):
    if a>b:
        a,b=b,a
    while a>0:
        c=b%a
        b=a
        a=c
    return b
def solve(a,b):
    c=gcd(a,b)
    cen=min(a,b)//c
    center=cen+2
    other=((a+1)*(b+1)-center)//2
    return center+other
a,b=map(int,input().split())
print(solve(a,b))