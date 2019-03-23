# This imports the argv module from the sys library
from sys import argv

# This gives two variables to argv (script and filename). Script is pulled directly from the name of the script and filename must be passed when triggering the script
script, filename = argv

# This gives users controls over the script (allowing them to continue or not)
print(f"We're going to erase {filename}.")
print("If you don't want that, hith CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# This offers the user the ability to input some string after the ?
input("?")

# This tells the use the file is being opened with the 'write' option
print("Opening the file...")
target = open(filename, 'w')

# this tells the user that the file is being emptied
# Tesitng wtih the w param in open() without truncate: print("Truncating the file. Goodbye!")
# target.truncate()

# this prompts the user to give content to the script for a new file
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# This lets the user know that a new file is being created with the previously entered content
print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n") # this is telling the script to enter a newline before the next input
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# too much repetition in the above 6 lines, trying to get it down to just 1 target.write command:
target.write('%r\n%r\n%r\n' % (line1, line2, line3))

# This closes the new file
print("And finally, we close it.")
target.close()
