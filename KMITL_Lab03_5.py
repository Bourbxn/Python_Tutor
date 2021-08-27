print(" *** Transform second ***")
seconds = input("Enter seconds : ")
try:
    seconds = int(seconds)
    print(seconds,"seconds : ",end='')
    week = seconds//(60*60*24*7)
    if week > 0: print(week,"weeks",end=' ')
    day = (seconds%(60*60*24*7))//(60*60*24)
    if day>0: print(day, "days",end=' ')
    hour = ((seconds%(60*60*24*7))%(60*60*24))//(60*60)
    if hour>0: print(hour, "hours",end=' ')
    minute = (((seconds%(60*60*24*7))%(60*60*24))%(60*60))//60
    if minute>0: print(minute,"minutes",end=' ')
    second = (((seconds%(60*60*24*7))%(60*60*24))%(60*60))%60
    if second>0: print(second,"seconds",end='')
    print("")
except:
    print("! ! ! please enter in whole number -->",seconds)
print(' --- program end ---')
