def moving_average(input_array):
	if len(input_array)<3:
		return []
	sum=input_array[0]+input_array[1]+input_array[2]
	result=0	
	for index in range(len(input_array)-2):
		if index!=0:
			sum=sum- input_array[index-1]+input_array[index+2]
		print("{0:.2f} ".format(sum/3), end='')
