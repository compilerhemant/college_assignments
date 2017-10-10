file_contents = open("input.txt","r")
test_cases = int(file_contents.readline().strip())
for i in range(test_cases):
	disjoint = 1
	dict1 = {}
	dict2 = {}
	for j in file_contents.readline().strip().split(' '):
		dict1[j] = True

	for j in file_contents.readline().strip().split(' '):
		dict2[j] = True

	if len(dict1)<len(dict2):
		for key, value in dict1.items():
			if dict2.get(key,False):
				disjoint = 0
	else:
		for key, value in dict2.items():
			if dict1.get(key,False):
				disjoint = 0
	if disjoint==0:
		print("NO")
	else:
		print("YES")
