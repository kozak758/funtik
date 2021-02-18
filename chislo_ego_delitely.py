####Ввести число, вывести все его делители.

print ("Input number, please:", end=" ")
n=int(input())
i=1
while i<=n:
    if n%i==0:
        print("Number divisors:",i)
    i+=1
   
