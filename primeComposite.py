num=input("Enter number to be checked :");
number=int(num);
for i in range(2, number):
	if(number%i==0):
		print("Entered number is not prime.");
		break
else:
	print("Enetered number is prime.");