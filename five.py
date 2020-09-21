pattern=[3,6,9,12]
selector=0
for i in range(1,101):
    modulo=i%15
    if modulo==0:
        print('fizzbuzz')
    else:
        if modulo==pattern[selector]:
            selector=(selector+1)%4
            print('fizz')
        elif modulo%5==0:
            print('buzz')
        else:
            print(i)
