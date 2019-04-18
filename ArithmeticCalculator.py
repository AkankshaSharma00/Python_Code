""" To make an arithmatic calculator that perform following operations
'+','-','*','/','%' using functions"""

#Function to perform '+' operation
def add(a,b):
	total = a+b
	print("Sum = ",total)
	return total

#Function to perform '-' operation
def sub(a,b):
	sub=a-b
	print("Difference = ",sub)
	return sub

#Function to perform '*' operation
def mul(a,b):
	mul=a*b
	print("Multiplication = ",mul)
	return mul

#Fuction to perform '/' operation
def div(a,b):
	div=a/b
	print("Division = ",div)
	return div

#Function to perform '%' operation
def mod(a,b):
	mod=a%b
	print("Modulus = ",mod)
	return mod

num1=eval(input("Enter First Number : "))
num2=eval(input("Enter Second Number : "))
print("Press 1 for Addition"+'\n'
	"Press 2 for Subtraction"+'\n'
	"Press 3 for Multiplication"+'\n'
	"Press 4 for Divide"+'\n'
	"Press 5 for Modulus")
oper=eval(input("Enter value of operation to be performed : "))
if oper==1:
	add(num1,num2)
elif oper==2:
	sub(num1,num2)
elif oper==3:
	mul(num1,num2)
elif oper==4:
	div(num1,num2)
elif oper==5:
	mod(num1,num2)
