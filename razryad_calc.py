r=int(input('Введите число: '))
r1=r
r=len(str(abs(r)))
print("Введенное число: ", r1, "является", r, "- значное!" , '\n')
rs=int(r)
rst=str(r1)

i=0
while r>=r-i:
   
    
    r2=10**(rs-1)
    r3=r//r2
    
    print("Разрядное Слагаемое:", rst[i])
    print("Разряд:", r2)
    i+=1
    rs-=1
    if i==r:
        
        break
