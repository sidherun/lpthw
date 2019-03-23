# This line imports argument variable module from the sys library
from sys import argv

# This line identifies the arguments required when the script runs
script, filename = argv

# This line initiates a variable, 'txt' and assigns the open function on the file we created 'ex15_samples.txt', which means the contents of the file are now represented by 'txt'
txt = open(filename)

# These lines print out the filename and then the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# These lines print out a request for the user to input the filename again and then give the '>' prompt for the user to give a filename to map to the file_again variable
# print("Type the filename again:")
# file_again = input("> ")

# This line assigns the variable txt_again to the contents of the variable 'file_again'
# txt_again = open(file_again)

# This line prints the contents of the variable 'txt_again'
# print(txt_again.read())
