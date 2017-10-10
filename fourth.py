file_contents = open("input.txt","r")
test_cases = int(file_contents.readline().strip())
for x in range(test_cases):
	array = file_contents.readline().strip().split(" ")
	dict = {}
# Logic
	for x in array:
		if dict.get(x,False):
			dict[x] = dict[x]+1
		else:
			dict[x] = 1
# output
	for key, value in dict.items():
		if value==2:
			print(key)
	print("\n")