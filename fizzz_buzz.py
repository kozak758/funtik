#У вас есть три числа, они вводятся из консоли.
#Первое число называется fizz, второе называется buzz. До
#третьего необходимо досчитать от единицы. Считая, надо выводить число.
#Если число кратно fizz - надо выводить F вместо числа.
#Если число кратно buzz - надо выводить B вместо числа.
#Если число кратно и fizz и buzz, надо выводить FB.
#И так - пока не будет достигнуто третье введенное число.

print("Enter number fizz:", end="")
n1=int(input())
print("Enter number buzz:", end="")
n2=int(input())
print("Enter the end number of the loop:",end="")
n3=int(input())
print("Array: ",end="")

i=1
while i<=18:
    if i%n1==0:
       print('F', end=" ")
    elif i%n2==0:
         print('B',end=" ")
    else:
            print(i, end=" ")
    if (i%n1==0 and i%n2==0):
        print('FB', end=" ")
    i+=1




