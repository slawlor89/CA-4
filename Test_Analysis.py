# Student number: 10354686
# CA 4 Programming for big data

# import the unit test functionality
import unittest

# import the functions created in the Analysis file
from Analysis import read_file, get_commits, get_authors, get_dates

# Create a class to extend the unit test class
class TestCommits(unittest.TestCase):
	# Create a function to call the read_file function
	def setUp(self):
		self.data = read_file('changes_python.log')
	
	# Create a function to test the length returned in the get_commits function
	def test_number_of_lines(self):
			self.assertEqual(5255, len(self.data))
	
	# Create a function to test the number of commits returned in the get_commits function
	def test_number_of_commits(self):
		commits = get_commits(self.data)
		self.assertEqual(422, len(commits))

	# Create a function to test the first line of the get_commits function
	def test_first_commit(self):
		commits = get_commits(self.data)
		self.assertEqual('r1551925', commits[0]['revision'])
		self.assertEqual('Thomas', commits[0]['author'])
		self.assertEqual('2015-11-27', commits[0]['date'])
		self.assertEqual('16:57:44', commits[0]['time'])
		self.assertEqual('1', commits[0]['number of lines'])
				
	# Creat a function to test the first author (I know this is just a repetition of the above)
	def test_first_author(self):
		commits = get_commits(self.data)
		self.assertEqual('Thomas', commits[0]['author'])
		self.assertEqual('r1551925', commits[0]['revision'])
	
# Create a function to test the get_authors function (test author and count results)
	def test_author_count(self):
		authors = get_authors(self.data)
		self.assertEqual(191, authors['Thomas'])
		self.assertEqual(152, authors['Jimmy'])
		self.assertEqual(1, authors['murari.krishnan'])
		self.assertEqual(5, authors['Alan'])
		self.assertEqual(7, authors['Freddie'])
		self.assertEqual(2, authors['Dave'])
		self.assertEqual(9, authors['ajon0002'])
		self.assertEqual(26, authors['Vincent'])
		
	# Create a function to test the first row of the get_dates function
	def test_date_count(self):
		dates = get_dates(self.data)
		self.assertEqual(4, dates['2015-10-16'])
		
if __name__ == '__main__':
    unittest.main()