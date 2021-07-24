
print("Enter 1st number.")
num1 = int(input())
print("Enter 2nd number.")
num2 = int(input())
divide = lambda num1,num2:num1/num2
multiply = lambda num1,num2:num1*num2
sum = lambda num1,num2:num1+num2
minus = lambda num1,num2:num1-num2

print("press 1 for Sum")
print("press 2 for Minus")
print("press 3 for Multiply")
print("press 4 for Divide")

choice = int(input())

if choice == 1:
    print(num1," + ",num2," = ",sum(num1,num2))
elif choice == 2:
    print(num1," - ",num2," = ",minus(num1,num2))
elif choice == 3:
    print(num1," * ",num2," = ",multiply(num1,num2))
elif choice == 4:
    print(num1," / ",num2," = ",divide(num1,num2))
else:
    print("Enter a valid choice.")
