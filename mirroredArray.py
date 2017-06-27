def main():
	A=[0,5,3,5,6]
	mirror(A)
def mirror(A):
	if len(A)<2:
		return print(-1)
	leftSum=0
	for item in A:
		leftSum+=item
	position=0
	missing=0
	rightSum=0
	length=len(A)
	while position<=len(A):
		rightSum+=missing
		missing=A.pop()
		leftSum-=missing
		if rightSum==leftSum:
			return print(length-position)
		position+=1
	return print(-1)
if __name__ == "__main__":
    main()