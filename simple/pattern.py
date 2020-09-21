pattern=['3','6','9','2','5','8','1','4','7','0']
index=0
for i in range(1,101):
    fb=''
    ones=str(i)[-1]
    if ones==pattern[index]:        
        fb='fizz'
        index+=1
        if index==10:
            index=0
    if ones=='5' or ones=='0':
        fb+='buzz'
    if fb=='':
        print(i)
    else:
        print(fb)
