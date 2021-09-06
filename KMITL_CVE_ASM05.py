lottoF=input("Enter lottery number : ")
lotto=lottoF
try:
    lottoF=int(lottoF)
    check=0
    Prize=[]
    if len(lotto)!=6: print("Wrong input !!!")
    else:
        if lotto=='046750' : Prize.append("First Prize")
        if (lotto[0]=='4' and lotto[1]=='2' and lotto[2]=='1'):
            Prize.append("Three Digit Prefix Prize")
        elif(lotto[0]=='6' and lotto[1]=='6' and lotto[2]=='6'):
            Prize.append("Three Digit Prefix Prize")
        if (lotto[3]=='1' and lotto[4]=='6' and lotto[5]=='0'):
            Prize.append("Three Digit Suffix Prize")
        elif (lotto[3]=='3' and lotto[4]=='5' and lotto[5]=='5'):
            Prize.append("Three Digit Suffix Prize")
        if (lotto[4]=='2' and lotto[5]=='3'):
            Prize.append("Two Digit Suffix Prize")
        if len(Prize)>0:
            print("You get ",end='')
            for i in range(len(Prize)):
                if i!=len(Prize)-1: print(Prize[i],end=', ')
                else: print(Prize[i])
        else:
            print("Sorry, You didn't get any Prize")
except:
    print("Wrong input !!!")
