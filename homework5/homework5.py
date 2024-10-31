def sum_numbers():
	total_sum = 0
	while True:
		try:
			print("Введите число или 'stop'/'end' для завершения: ")
			input_value = input()
			if input_value=='stop' or input_value=='end':
				break
			total_sum += float(input_value)
		except ValueError:
			print("Неверный ввод")
	print("Сумма всех введенных чисел:",total_sum)

sum_numbers()
