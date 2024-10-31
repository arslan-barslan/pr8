def numbers(a, b):
	if not isinstance(a, int) or not isinstance(b, int):
		print("Одно из чисел не подходит")
		raise ValueError
	if b < a:
		a, b = b, a
	for i in range(a, b + 1):
		print(i)
try:
	print("Введите первое число ")
	a = int(input())
	print("Введите второе число ")
	b = int(input())
	print("Все целые числа, расположенные между ними")
	numbers(a, b)
except ValueError:
	print("Ввод должен быть в формате целого числа")

