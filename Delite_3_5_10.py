#Проверить, является ли число нечетным,
#делится ли на три и на пять одновременно, но так,
#чтобы не делиться на 10.
print ("Input number:", end=" ")
number=int(input());
if number%2==0:
    print("The number is Even!!")
elif (number%3==0 and number%5==0 and number%10!=0):
    print("Perfect! This number fits the condition of the problem.")
else:
    print("Sorry!! This number does not fit the condition of the problem.")

