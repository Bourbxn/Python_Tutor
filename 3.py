date, add_day1, add_day2=input("Enter date add_day : ").split()
dd=int(date[0:2])
mm=int(date[2:4])
yyyy=int(date[4:8])
add_day1=int(add_day1)
add_day2=int(add_day2)
sum_day=add_day1+add_day2
print("---Date---")
print("dd   =",dd)
print("mm   =",mm)
print("yyyy =",yyyy)
for i in range(sum_day):
    dd+=1
    if dd>=31:
        dd=1
        mm+=1
    if mm>=13:
        mm=1
        yyyy+=1
print("---New Date---")
print("dd   =",dd)
print("mm   =",mm)
print("yyyy =",yyyy)
