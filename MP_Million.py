#Matt Parker Math Sumbissions? 
#JC Tecklenburg
# https://www.youtube.com/watch?v=ILrqPpLpwpE
# MY "I" and "O" keys stick sometimes so sorry for the spelling! 

#returns array with all splits of final number balances
def buildArray(endNum):
	outputArray = []
	for i in range(endNum-1):
		num = i+1
		inverseNum = endNum-num
		if num <= inverseNum:
			entry = [num, endNum-num]
			outputArray.append( entry )
		else:
			break
	print("Splits Buiilt")
	return outputArray

#flip array element positions
def flipArrayElements(array, id1, id2):
	temp = array[id1];
	array[id1] = array[id2]
	array[id2] = temp
	return array

#derive the rest of the fibinachi sequence deposits
def continueFib(array):
	while array[0] > 1:
		nextNum = array[1]-array[0]
		array.insert(0,nextNum)
	#remove negative values
	if array[0] < 1:
		array.pop(0)
	# if array[0] > array[1]:
	# 	flipArrayElements(array,0,1)
	return array

#derive deposits for the splits array
def splitsFib(array):
	for entry in array:
		continueFib(entry)
	print("Derived Deposts")
	return array	

#get the second deposit
def getSecondDeposit(array):
	return array[1]-array[0]

def getBothDeposits(array):
	return [array[0], getSecondDeposit(array)]

if __name__ == "__main__":
	print("Bleep Boop!")
	length=0;
	longestSolutions = []
	for entry in splitsFib( buildArray(33) ):
		if len(entry) == length:
			longestSolutions.append(entry)
		if len(entry) > length:
			length = len(entry)
			longestSolutions = []
			longestSolutions.append(entry)
	print("The longest entry is", length, ".")
	for solution in longestSolutions:
		print(solution)
		print(getBothDeposits(solution))
	# buildArray(13)
	# print(buildArray(13))