# Implement this as well, open a generic file through command line?
# Evrything is good except that I have yet not decided how to deal with floats?
# How about directly creating the dictionary instead of making an array?
file_contents = open("input.txt","r")
test_cases = int(file_contents.readline().strip())

for i in range(test_cases):
	sum = int(file_contents.readline().strip())
	array = file_contents.readline().strip().split(' ')
	# creating dictionary
	dict = {}
	for j in range(len(array)):
		dict[array[j]] = True
	found = 0

	# checking for duplicate entries
	double = 0
	for x in range(len(array)):
		if int(array[x])==sum/2:
			double = double + 1
	
	if double>1:
		print(str(int(sum/2))+" "+str(int(sum/2)))
		found = 1
	
	# main logic
	for k in range(len(array)):
		otherNum = sum - int(array[k])
		dict.pop(array[k],0)
		if dict.get(str(otherNum),False):
			found = 1
			print(array[k]+" "+str(otherNum))
			dict.pop(str(otherNum),0)
			dict.pop(array[k],0)
	# Not found
	if found==0:
		print ("No such pair exists")