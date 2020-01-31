import calc
op = input('enter the operators')
num = input('enter the number')
x = (int(i) for i in num.split(","))
print(calc.calculator[op](x[0], x[1]))