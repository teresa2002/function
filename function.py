def wash(dry=False, water=8):
	print('加水',water,'分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

wash(True, water=10) #使用function




def add(x, y):
	return x + y
result = add(3, 4)
print(result)


def average(numbers):
	return sum(numbers)/ len(numbers)

print(average([1,2,3]))
print(average([1111, 2232, 456]))
print(average([456, 789 ,941]))