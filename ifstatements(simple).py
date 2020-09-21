for i in range(100):
    j=''
    if i%3==0:
        j+='fizz'
    if i%5==0:
        j+='buzz'
    if j=='':
        j+=str(i)
    print(j)
