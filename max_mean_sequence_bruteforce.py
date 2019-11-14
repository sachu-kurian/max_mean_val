# random list of values
lst = [5, 10, 9, 7, 3, 8, 6]

max_mean = 0
max_mean_sequence = []
block_size_start = 1 #this will always give the max value of list as mean if set to 1

print("Original List:{}".format(lst))

# first loop to increment the values of block each time
for block_size in range(block_size_start, len(lst)+1):
	print("====Block Size - {}====".format(block_size))
	
	# second loop to get the index position till size of list - size of block
	for index in range(len(lst)-block_size+1):
		print(lst[index:index+block_size])
		mean_val = sum(lst[index:index+block_size])/block_size 
		if mean_val >= max_mean:
			max_mean = mean_val
			max_mean_sequence = lst[index:index+block_size]
			
print("Max Mean=", max_mean)
print("Max sequence:", max_mean_sequence)
