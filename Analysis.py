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

# Let's create an array which will start off as blank
commits = []
# Then lets start with a row index of zero which we will use to work through the file
row_index = 0
# Find the first line in the file and split out based on the pipe delimeter
details = data[row_index + 1].split('|')
# Create a dictionary object to assign each of the values
commit = {'Revision': details[0].strip(),
          'Author': details[1].strip(),
          'Date': details[2].strip(),
          'Number of lines': details[3].strip().split(' ')[0]}

# Add the commit object to the commits array
commits.append(commit)

# Print the commits array to ensure that it is working correctly
print commits