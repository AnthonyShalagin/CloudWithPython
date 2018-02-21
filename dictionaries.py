cats =   {} #dictionaries
a_list = [] #lists


cats["Robin"] = 5
cats["Adrian"] = 3


print(cats["Adrian"])
print(cats.get("Adrian"))
#print(cats['hi']) #Key Error

for name in cats:
	print(name, cats[name])

del cats["Robin"]
print(cats.pop("Adrian"))

for name in cats.keys():
	print(name, cats[name])

for num_cats in cats.values():
	print(num_cats)


#None (no value of null)

my_data = " "

if my_data: 
	print(my_data)		# Won't print

my_data = None

#if my_data is None: 
	#print('Not set')