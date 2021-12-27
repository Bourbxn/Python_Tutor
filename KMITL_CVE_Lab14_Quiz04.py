def diff(a, b):
    x = int(b[0]) - int(a[0])
    y = int(b[1]) - int(a[1])
    return "(%d, %d)" % (x, y)


print("  Find difference between A(x1,y1) and B(x2,y2) ")
ins = input("Enter x1 y1 x2 y2 : ").split()
pointA = (int(ins[0]), int(ins[1]))
pointB = (int(ins[2]), int(ins[3]))
print("A B ==>", pointA, pointB)
print("Differnce from", pointA, "to", pointB, "==>", diff(pointA, pointB))
print("Differnce from", pointB, "to", pointA, "==>", diff(pointB, pointA))
