import sys

if __name__ == "__main__":

	# remove line 1 header from csv file first

	# count # of unique items in col 2
	# count # of items in col 3

	# process file from input
	input = sys.argv[1]
	print input

	# read file
	f = open (input, "r")
	content = f.read()

	# delimit lines
	lines = content.split("\r",)

	countEnrollmentDict = {}
	countSectionDict = {}

	for line in lines:
		elements = line.split(",",)

		# get enrollment numbers into dict
		enrollElement = elements[2]
		if countEnrollmentDict.get(enrollElement) == None:
			countEnrollmentDict[enrollElement] = 1
		else:
			val = countEnrollmentDict.get(enrollElement) + 1
			countEnrollmentDict[enrollElement] = val

		# get section number into dict
		sectionElement = elements[1]
		if countSectionDict.get(sectionElement) == None:
			countSectionDict[sectionElement] = 1
		else:
			val = countSectionDict.get(sectionElement) + 1
			countSectionDict[sectionElement] = val

	print "number of sections : " + str(len(countSectionDict))

	sum = 0
	for items in countEnrollmentDict:
		sum += countEnrollmentDict.get(items)
	print "total enrollment : " + str(sum)

