# This is an improved version of first number Mastermind Game
# Purpose is to learn Python coding and have cleaner code than first try

#Import random generator
from random import randint

#Generate five random digits
def rand_number():
	randomized = [(randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9)), (randint(0,9))];
	#Print randomized numbers
	print randomized
	return randomized

#Ask five digits from user
def guess_from_user():
	input = raw_input("Give 5 digits: ") #This takes input
	return input
	
	
#Check that input only has 5 digits and put number in list as integers
def has_5_digits(input):
	while len(str(input)) != 5:
		print input
		input = guess_from_user()
	five_digit_input = [int(input[0]), int(input[1]), int(input[2]), int(input[3]), int(input[4])]
	print five_digit_input
	return five_digit_input

#Compare master_number and guessed
def compare_numbers(input,rand):
	#print input
	#print rand
	if input == rand:
		print "Correct answer! You're mastermind"
	else:
		print "Not correct"

#How many numbers are in correct place
def right_place_number(input,rand):
	n=0
	right_place = 0
	
	while n < 5:
		if input[n] == rand[n]:
			right_place = right_place + 1
		n = n + 1
	return right_place

#How many correct number but wrong place
def right_number_wrong_place (input,rand):
	n = 0
	s = 4
	right_number = 0
	
	while n < 5:
		if n != s and input[n] == rand[s]:
				right_number = right_number + 1
		n = n + 1
		s = s - 1
	return right_number			
	


master_number = rand_number()
guessed = guess_from_user()
valid_guess = has_5_digits(guessed)
compare_numbers(valid_guess,master_number)
print "Numbers in right place: ", right_place_number(valid_guess,master_number)
print "Right number but wrong place: ", right_number_wrong_place(valid_guess,master_number)
