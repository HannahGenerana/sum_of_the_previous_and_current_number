# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
 
# pseudocode

print ("Printing the current number as well as the previous number and their sum in a range.")

# set the previous number to 0
previous_number = 0

# create a loop 
for current_number in range (0,11):

# add the current and previous number
    total_sum = previous_number + current_number

# print the list of current number, previous number, and their sum
    print (f"Current number : {current_number} Sum : {total_sum}")

# change the value of previous number to current number