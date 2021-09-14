def isValidWeightHeight(a,b):
    if((a>0 and a<=200) or (b>0 and b<=300)):
        return True
    else:
        return False

def bmiCalculator(a,b) :
    bmi= a/((b/100)*(b/100))
    if bmi<18.5:
        print("underweight")
    elif (bmi>=18.5 and bmi<=22.9):
        print("normal")
    else:
        print("overweight")

a,b = input("Enter weight(kg) and height(cm): ").split()
try:
    a,b = float(a),float(b)
except:
    print('Not number')
    quit()
if isValidWeightHeight(a,b):
    print('You are',end=' ')
    bmiCalculator(a,b)
else:
    print('Not valid weight or height.')