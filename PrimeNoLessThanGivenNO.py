num=eval(input("Enter number : "))
for i in range(1,num):
	# print(i)
	for j in range(2,i):
		print(j)
		if num%j==0:
			print(i,j)
		# else:
		# 	pass
		# 	