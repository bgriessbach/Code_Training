input=[int(a_temp) for a_temp in input().strip().split(' ')]
k=input[2]
day_array=list(range(input[0],input[1]+1))
result=0
for item in day_array:
    reverse=(int((str(item)[::-1])))
    if abs(reverse-item)%k==0:
        result+=1
print(result)
