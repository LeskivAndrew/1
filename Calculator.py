#Programm-calculator with functions of addition, subtraction, multiplication, division
print ('Hello! Im a programm - calculator!')
variable=True
#c ='+'
while variable:
    a = int(input('Please input first number from 0 to 1000000000000 '))
    while a<0 or a>1000000000000:
        a = int(input('Wrong number, input again!'))
    else:
        b = int(input('Please input second number from 0 to 1000000000000 '))
        while b < 0 or b > 1000000000000:
            b = int(input('Wrong number, input again!'))
        else:
            c = input ('Choose necessary arithmetic operation: +,-,*,/ ')
            while c!='+' and c!='-' and c!='*' and c!='/':
                c = input ('Error, input correct operation: +,-,*,/ ')
            else:
                variable = False
                if c=='+':
                    result = a+b
                    print (f'{a} {c} {b} = {result}')
                    variable=False
                if c=='-':
                    result = a-b
                    print (f'{a} {c} {b} = {result}')
                    variable = False
                if c== '*':
                    result = a*b
                    print (f'{a} {c} {b} = {result}')
                    variable = False
                if c== '/':
                    result = a/b
                    print (f'{a} {c} {b} = {result}')
                    variable = False