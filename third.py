file_contents = open("input.txt","r")
test_cases = int(file_contents.readline().strip())
for x in range(test_cases):
	array = file_contents.readline().strip().split(" ")
	sumWasZero = 0
	sumChanged = 0
	for x in range(0,len(array)):
		for y in range(0,len(array)):
			sum = 0
			if y+x > len(array)-1:
				break
			else:
				for z in range(x+1):
					sum = sum + int(array[y+z])
					if sum == 0:
						sumWasZero = 1
					sumChanged = 1

	if sumWasZero==1 and sumChanged == 1:
		print("YES")
	else:
		print("NO")