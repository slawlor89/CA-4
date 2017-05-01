# Student number: 10354686
# CA 4


# Step 1. Read the file into an object called data
# Assign a name to the file
changes_file = 'changes_python.log'
# Read in the file and remove any spaces from each of the lines
data = [line.strip() for line in open(changes_file, 'r')]

# Determine the number of lines of the file read in
print (len(data))

# Based on visually reviewing the file, we can see that the separator between each of the commits is 72 hyphens in a row
# Create an opject called separator to define 72 hyphens
separator = 72*'-'

