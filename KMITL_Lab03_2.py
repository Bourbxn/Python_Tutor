print(" *** Min Max Avg ***")
a,b,c=input("Enter 3 number : ").split()
a=float(a)
b=float(b)
c=float(c)
if (a>=b and a>=c):
    max=a
    if b>=c: 
        mid=b
        min=c
    else: 
        mid=c
        min=b
elif(b>=a and b>=c):
    max=b
    if a>=c:
        mid=a
        min=c
    else: 
        mid=c
        min=a
elif(c>=a and c>=b):
    max=c
    if a>=b:
        mid=a
        min=b
    else :
        mid=b
        min=a
print("min, mid, max ==> %.2f, %.2f, %.2f"%(min,mid,max))
print("Average ==> %.2f"%((a+b+c)/3))
#Hello