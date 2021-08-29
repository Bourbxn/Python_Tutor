def find_digit(digit):
    OnetoNine = ["one","two","three","four","five","six","seven","eight","nine"]
    for i in range(10):
        if i==digit-1:
            print(OnetoNine[i],end='')

def num_to_word(num):
    while num!=0:
        if num//10**11!=0:
            find_digit(num//10**11)
            if num%(10**11)==0: print(" hundred billion",end='')
            else: print(" hundred",end=' ')
            num%=(num//10**11)*(10**11)
        elif num//10**10!=0:            #pick
            if num//10**10==1:
                TentoNineteen=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                "eighteen","nineteen"]
                for i in range(10,20,1):
                    if i==num//(10**9): 
                        if num%(10**9)==0:print(TentoNineteen[i-10],end=' billion')
                        else: print(TentoNineteen[i-10],end=' billion ')
                num%=(num//10**9)*(10**9)
            else:
                TwentytoNinety=["twenty-","thirty-","forty-","fifty-","sixty-","seventy-","eighty-","ninety-"]
                for i in range(2,10,1):
                    if i==num//10**10: print(TwentytoNinety[i-2],end='')
                num%=(num//10**10)*(10**10)
        elif num//10**9!=0:
            find_digit(num//10**9)
            if num%(10**9)==0: print(" billion",end='')
            else: print(" billion",end=' ')
            num%=(num//10**9)*(10**9)
        elif num//10**8!=0:
            find_digit(num//10**8)
            if num%(10**8)==0: print(" hundred million",end='')
            else: print(" hundred",end=' ')
            num%=(num//10**8)*(10**8)
        elif num//10**7!=0:         #pick
            if num//10**7==1:
                TentoNineteen=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                "eighteen","nineteen"]
                for i in range(10,20,1):
                    if i==num//(10**6): 
                        if num%(10**6)==0:print(TentoNineteen[i-10],end=' million')
                        else: print(TentoNineteen[i-10],end=' million ')
                num%=(num//10**6)*(10**6)
            else:
                TwentytoNinety=["twenty-","thirty-","forty-","fifty-","sixty-","seventy-","eighty-","ninety-"]
                for i in range(2,10,1):
                    if i==num//10**7: print(TwentytoNinety[i-2],end='')
                num%=(num//10**7)*(10**7)

        elif num//10**6!=0:
            find_digit(num//10**6)
            if num%(10**5)==0: print(" million",end='')
            else: print(" million",end=' ')
            num%=(num//10**6)*(10**6)
        elif num//10**5!=0:
            find_digit(num//10**5)
            if num%(10**5)==0: print(" hundred thousand",end='')
            else: print(" hundred",end=' ')
            num%=(num//10**5)*(10**5)
        elif num//10**4!=0:         #pick
            if num//10**4==1:
                TentoNineteen=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                "eighteen","nineteen"]
                for i in range(10,20,1):
                    if i==num//(10**3): 
                        if num%(10**3)==0:print(TentoNineteen[i-10],end=' thousand')
                        else: print(TentoNineteen[i-10],end=' thousand ')
                num%=(num//10**3)*(10**3)
            else:
                TwentytoNinety=["twenty-","thirty-","forty-","fifty-","sixty-","seventy-","eighty-","ninety-"]
                for i in range(2,10,1):
                    if i==num//10**4: print(TwentytoNinety[i-2],end='')
                num%=(num//10**4)*(10**4)

        elif num//10**3!=0:
            find_digit(num//10**3)
            if num%(10**2)==0: print(" thousand",end='')
            else: print(" thousand",end=' ')
            num%=(num//10**3)*(10**3)
        elif num//10**2!=0:
            find_digit(num//10**2)
            if num%(10**2)==0: print(" hundred",end='')
            else: print(" hundred",end=' ')
            num%=(num//10**2)*(10**2)
        elif num//10**1!=0:
            if num//10==1:
                TentoNineteen=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                "eighteen","nineteen"]
                for i in range(10,20,1):
                    if i==num: print(TentoNineteen[i-10],end='')
                num=0
            else:
                TwentytoNinety=["twenty-","thirty-","forty-","fifty-","sixty-","seventy-","eighty-","ninety-"]
                for i in range(2,10,1):
                    if i==num//10: print(TwentytoNinety[i-2],end='')
                num%=(num//10**1)*(10**1)
        elif num//1!=0:
            find_digit(num%10)
            num=0

if __name__ == '__main__':
    numIn=int(input())
    num_to_word(numIn)
