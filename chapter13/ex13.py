# “ This is how we add modules to your script from the Python feature set.”
# argv variable holds the arguments we pass to our Python script when you run it.
from sys import argv
# “unpacks” argv so that, rather than holding all the arguments, it gets assigned to four variables we can work
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Input
# “python3.6 ex13.py first 2nd 3rd
# Output
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd”
