def triangleChecker(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if(a==0 or b==0 or c==0):
        print("Side of triangle must not be zero.")
    elif(a<0 or b<0 or c<0):
        print("INPUTs cannot be negative.")
    elif (a+b<=c or a+c<=b or c+b<=a):
        print("NOT VALID sides")
    elif(a==b and a==c and b==c):
        print("equilateral triangle")
    elif ((a==b)or(b==c)or(a==c)):
        print("isosceles triangle")
    elif(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
        print("right triangle") 
    else:
        print("triangle")
    
print(" Triangle Checker ***")
a,b,c = input("Enter side1 side2 side3 : ").split()
triangleChecker(a,b,c)