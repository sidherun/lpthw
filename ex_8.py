formatter = "{} {} {} {}" #defining the string 'formatter'

print(formatter.format(1, 2, 3, 4)) #passing 1,2,3,4 to the format() function: see https://www.programiz.com/python-programming/methods/built-in/format
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a Poem",
    "Or a song about fear"
))
