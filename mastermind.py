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
	if input == correct:
		print input
		print correct
		print "It is same"
		return True
	else:
		print input
		print correct
		print "Not same"
		return False

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
compare(input_list, correct_answer)

#print (randint(0,9))
	
	
