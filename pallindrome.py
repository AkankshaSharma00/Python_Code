number=eval(input("Enter number :"))
num=number
rev=0
for numbers in str(number):
	rev=(rev*10)+(num%10)
	num//=10
	print ("test",number,rev)
if number == rev :
	print(str(number)+" is a pallindrome");
else:
	print(str(number)+ " is not a pallindrome");