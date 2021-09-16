# Information-Retrieval (Inverted Indexing)

Name: Neeraj Dusa

Steps to execute my file:

1. Install nltk and after installation, in nltk.stem, import PorterStemmer.
2. Give a correct path to the dataset directory in the main function to perform the tasks correctly.
3. Type "python3 InvIndexing.py" in terminal
4. One can see an output file in the name: "InvIndexing-output.txt"



Important Details :

* Data structures used in code - Arrays and Hash Tables

* Time Complexity - 
	Initially - O(n*p*q) where  
	n => Total no of txt files 
	p => Words per document
	q => Average word-size 
	n*p*q => total no of characters in all documents
	As, q is almost negligible
	Hence, Time complexity is O(n*p)

* Space Complexity -
	m =>  Unique words 
	n => Number of text files
	Hence, Space complexity is O(m*n)



Implementation Explanation :

* class listpost:
Explanation:
This class will take document id and its frequency and create a seperate posting list.

* class invIndex:
Explanation:
This class will do inverted indexing of all words of all files.

* def process_word(self, chars):
Explanation:
This function replaces special characters with space or empty.

* def file_processor(self, file_name, cont):
Explanation:
This function extracts words from each file and counts the frequency of each word.

* def index_of_directory(self, path_of_dir):
Explanation:
This function extracts each file from folder and sends each file to process_file function.

* def to_export_index(self, output_file_name="Assign012019047-output"):
Explanation:
This function exports the output of each item in posting list to a new output file.
