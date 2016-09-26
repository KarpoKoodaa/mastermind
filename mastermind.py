# This is a number mastermind game 
# Purpose is to learn python coding

from random import randint #This imports random integer

def rand_number():
	#This function randomise 5 numbers
	correct_answer = [(randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9))];
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
	if len(str(input)) > 5:
		input_from_user()		
	return False

#print input_from_user()
#guess = input_from_user()
print check_if_correct(input_from_user())

print rand_number()
	

#print (randint(0,9))
	
	
