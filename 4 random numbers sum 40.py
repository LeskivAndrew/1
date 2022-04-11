import random
a=[0, 0, 0, 0, 0, 0, 0]
b=False
c=0
while b<1:
    for i in range (7):
        a[i]=random.randint(1, 10)

    c+=1
    if sum(a) == 40:
         print(f'list of random numbers equal to 40: {a}')
         print (f'Numbers of ramdoms: {c}')
         b=True








