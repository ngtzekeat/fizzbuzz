bigtext=''
j=0
while True:
    for i in range(2):
        j+=1
        bigtext+=(str(j)+'\n')
    j+=1
    bigtext+='fizz\n'
    if j==99:
        bigtext+='100'
        break
bigtext2=bigtext.split('\n')
print(bigtext2)
bigtext=''
f=1
for i in bigtext2:
    if 50<f<60:
        if f==55:
            bigtext+='buzz\n'
        else:
            bigtext+=i+'\n'
    else:
        if '5' in str(f) or '0' in str(f):
            if f%15==0:
                bigtext+='fizzbuzz\n'
            else:
                bigtext+='buzz\n'
        else:
            bigtext+=i+'\n'
    f+=1
print(bigtext)
    
    
