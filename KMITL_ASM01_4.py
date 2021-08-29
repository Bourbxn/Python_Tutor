hour,minute,second=input("Enter Parking Time : ").split()
hour=int(hour)
minute=int(minute)
second=int(second)
second+=((minute*60)+(hour*3600))
if second<=15*60:price="FREE"
elif(second>15 and second<=4*3600):
    price=(second//3600)*10
    if second%3600>0: price+=10
elif(second>4*3600 and second<=6*3600):
    price=40
    price+=((second-3600*4)//3600)*20
    if second%3600>0: price+=20
elif second>6*3600:
    price=(second//(3600*24))*200
    if second%(3600*24)>0: price+=200
print("Parking Fee is",price)