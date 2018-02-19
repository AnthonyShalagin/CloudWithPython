def noop():
	pass

def greet(name):
	print("Hello, {0}".format(name))

greet("Anthony")

def product(numbers):
	p = 1
	for n in numbers:
		p = p * n
	print p

product([1,2,3,4,5])

def combine_and_sort(first, second):
	return sorted(first+second)

print(combine_and_sort([1,3,5], [2,4,6]))


nums = [20,25,22,21,23]
sorted(nums) 				#not in place
print(nums)
nums.sort()					#in place
print(nums)
