# This is a number mastermind game 
# Purpose is to learn python coding

from random import randint #This imports random integer

def rand_number():
	#This function randomise 5 numbers
	correct_answer = [(randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9))];
	print correct_answer
	return correct_answer

def input_from_user():
	#This function asks input from user
	input = raw_input("Give 5 digits: ")
	#str(input)
	#lenght = len(str(input))
	#print lenght
	return input

def check_if_correct(input):
	#This checks that input has 5 digits and no more
	while len(str(input)) != 5:
		print input
		input = input_from_user()		
	return input

def compare(input, correct):
	# Compares if input from user is same as randomised number
	i = 0
	right_place = 0
	right_number = 0
	s = 1
	n = 0
	t = 0
	if input == correct:
		print input
		print correct
		print "Correct, you're mastermind of masterminds"
		return True
	
	else:
		while n < 5:
			if input[0] == correct[i]:
				right_place = right_place + 1
			
			else:
				s = 0
				while s < 5:
					if input[0] == correct[s]:
						right_number = right_number + 1
				s = s + 1
					
		n = n + 1
	
	
	"""else:
		while n < 5:
			while i < 5:
				if input[n] == correct[i]:
					right_place = right_place + 1
				else:
					while s < 5:
						if input[n] == correct[s]:
							right_number = right_number + 1
							s = s + 1
						else:
							#n = n+1 
							s = s + 1
					
			#print "input: ", input[i]
			#print "correct: ",correct[i]
			#print "Right Place: ",right_place
			#print "Right Number: ", right_number
				i = i + 1 """
			#n = n + 1 	
			#t = t + 1
			#print t
	return {'rp' : right_place, 'rn' : right_number}
		 
			
		#print input
		#print correct
		#print "Not same"
		#return False

#print input_from_user()
#guess = input_from_user()
#print check_if_correct(input_from_user())
#print rand_number()
correct_answer = rand_number()
input1 = input_from_user()
check_if_correct(input1)
input_list = [int(input1[0]), int(input1[1]), int(input1[2]), int(input1[3]), int(input1[4])]
#print type(input_list[0])

#print type(correct_answer[0])
print input1
print input_list
print correct_answer
#print rand_number()
rights = compare(input_list, correct_answer)

print rights
#print rights["rp"][0]
#print rights["rn"][0]
#right_place_final = right_place
#right_number_final = right_number
print "Right numbers: " , rights ["rn"]
print "Numbers in right places:" , rights ['rp']

#print (randint(0,9))
	
	
