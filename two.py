i=0
three=0
five=0
while True:
    text=''
    i+=1
    three+=1
    five+=1
    if three==3:
        three=0
        text+='fizz'
    if five==5:
        five=0
        text+='buzz'
    if text=='':
        text=str(i)
    print(text)
    if i==100:
        break
