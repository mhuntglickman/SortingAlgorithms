"""
Test Cases:
[0,1,2,3,4]
[3,6,1,5,9]
"""

def sortInsertion(lst):

	for i in range(1,len(lst)):
		
		# the i is the index of the item we are currently checking and has to be 
		# assigned to a value so we can track it and eventually insert it
		value = lst[i]  # value = 1

		index = i  # index = 2

		while index > 0 and lst[index-1] > value:
			# 0 > 0 auto fail break out of loop

			# the sorted item needs to move right so we are increasing the 
			# size of the sorted array and making room for eventually inserting
			# our value
			lst[index] = lst[index-1]
			# lst[1] = 3
			# lst[3,3,6,5,9]
			# lst[3,6,6,5,9]

			index = index-1
			# index = 1-1 = 0

		lst[index] = value
		# lst[index] = 1

		# lst[1,3,6,5,9]