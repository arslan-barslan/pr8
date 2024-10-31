
error=['Неверное значение в 1 числе','Неверное значение в 2 числе']
print("exit или stop чтобы выйти")
while True:
	try:
		flag=0
		print("Введите первое число")
		x=input()
		if x=="exit" or x=="stop":
			break
		x=int(x)
		print("Введите второе  число")
		y=input() 
		if y=="exit" or y=="stop":
			break
		flag+=1
		y=int(y)
		print("Сумма числа равно:",x+y) 
	except ValueError:
		print(error[flag])
