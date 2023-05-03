# Generator
import random

# Test data
array = [random.randint(-10, 20) for i in range(random.randint(6, 28))]
number = random.randint(-10, 25)

# Manual input
# array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# number = int(input(f"Введите любое число: "))
len_array = len(array)-1

'''
Условие:
Далее программа работает по следующему алгоритму:
Преобразование введённой последовательности в список
Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
Устанавливается номер позиции элемента, который меньше введенного пользователем числа, 
а следующий за ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, 
который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
'''


def insertion_sort(input_array):
	for i in range(1, len(input_array)):
		x = input_array[i]
		idx = i
		while idx > 0 and input_array[idx-1] > x:
			input_array[idx] = input_array[idx-1]
			idx -= 1
		input_array[idx] = x
	return input_array


def binary_search_for_smaller_value(input_list, element, left, right):
	middle = (right + left) // 2  # находимо середину
	if left > right:   # если левая граница превысила правую
		return middle if element > input_list[middle] else None

	if element == input_list[middle]:
		if middle == 0:  # первый элемент равный искомому
			return None
		# рекурсивно ищем в значение строго меньше
		return binary_search_for_smaller_value(input_list, element, 0, middle-1)

	elif element < input_list[middle]:  # если элемент меньше элемента в середине
		# рекурсивно ищем в левой половине
		return binary_search_for_smaller_value(input_list, element, left, middle - 1)
	else:  # иначе в правой
		return binary_search_for_smaller_value(input_list, element, middle + 1, right)


print(f'Введённой список {array}')
print(f'Введенное число {number}')

array = insertion_sort(array)
print(f'Сортированный список {array}')

if array[0] <= number <= array[len_array]:
	index_number = binary_search_for_smaller_value(array, number, 0, len_array)
	if index_number is None:
		print(f'Номер позиции элемента меньше {number} не найден')
	else:
		print(f'Номер позиции меньше пользовательского числа: {index_number}')
		print(f'Значение найденного элемента: {array[index_number]}. Введенное число: {number}')
else:
	print('Число за пределами списка')