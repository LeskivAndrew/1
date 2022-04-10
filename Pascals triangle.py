#Pascal's triangle
n=int(input ('Input number of strings '))
a=2
b=0
res1 = [1]
res2 = [1,1]
print (res1)
print (res2)
res1=[]
while a < n:
    res1.append (1)
    for i in range (1,a):
        res1.append (res2[i-1]+res2[i])
    res1.append (1)
    print (res1)
    res2=res1
    res1=[]
    a+=1

"""for i in range (0,n):
    result.append(1)
    print (result)"""



