# Student number: 10354686
# CA 4

# Define a function to read in the file and strip into lines
def read_file(changes_file):
    # Read in the file and remove any spaces from each of the lines
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

# Define a function to get the details related to the strip    
def get_commits(data):
    separator = 72*'-'
    commits = []
    row_index = 0
    while row_index < len(data):
        try:
            # Find the first line in the file and split out based on the pipe delimeter
            details = data[row_index + 1].split('|')
            # Create a dictionary object to assign each of the values
            commit = {'Revision': details[0].strip(),
            'author': details[1].strip(),
            'date': details[2].strip().split(' ')[0],
            'time': details[2].strip().split(' ')[1],
            'number of lines': details[3].strip().split(' ')[0],
            'comment': data[row_index+2:data.index('',row_index+1)]}

            # Add the commit object to the commits array
            commits.append(commit)
            # Update the index
            row_index = data.index(separator, row_index + 1) # Search for the separator from the current index plus one
        except: # This except line is for the index out of range error that will happen at the end of the file. Expected error
            break
    return commits

# Create an empty array for authors




   
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)


    
# Statistical conclusion #1: There are a total of 422 commits as part of the file
number_of_commits = str(len(commits))
print 'There are:',number_of_commits,'commits in the file'

# Statistical conclusion #2: How many commits were there per author
authors = {}
for commit in commits:
	author = commit['author']
	if commit['author'] not in authors:
		authors[author] = 1
	else:
		authors[author] = authors[author] + 1

print authors

# Statistical conclusion #3: How many commits were there per day
dates = {}
for commit in commits:
	date = commit['date']
	if commit['date'] not in dates:
		dates[date] = 1
	else:
		dates[date] = dates[date] + 1

print dates
