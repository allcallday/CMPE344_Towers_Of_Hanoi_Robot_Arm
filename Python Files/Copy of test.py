#print program welcome message
print ("===Hello, Python!===");

# declare and initialize variables
counter = 100;		#var names must be lower case
miles = 1000.0;		#var types implied by assigned value
name = "John";
aNumber = 0;



# print variables
print (counter);
print (miles);
print (name);



# take an integer input from user and output the result
aNumber = int(input("Enter an integer: "));	#input()
print ("You entered:");
print (aNumber);



# if-else branch based on user input
if (aNumber < 5) : print ("Your number is less than 5");
else : print ("Your number is not less than 5");



# for loop test
print ("This loop to print numbers 0 - 7:");
for num in range(0,8):
	print (num);
print ("loop has ended");



# while loop test
ctrl = 0;
while ctrl != 8:
	print("You are in an infinite while loop. Enter 8 to exit.");
	ctrl = int(input());
	
	
	
# break, continue, pass statement demo
for letter in "Python":		#loop through characters in string and break when 'h' is encountered
	if letter == 'h':
		break;
	print("Spelling 'Python' w/ break: ", letter);
#continue;
#pass;

	
	
# simple bubble sorting algorithm implementation
listToSort = [2, 3, 6, 1, 5, 4, 7, 8];	# declare and initialize variables
print("Unsorted list:");	# print list before sorting
for num in listToSort:	#loop to print each number in the list
	print (num);
print("Now sorting list...");
for iter_num in range(len(listToSort)-1,0,-1):		#iter_num is any var name;	range() is a method w/ three parameters [starting number of seq.], [generate numbers up to, but not including this num], and 
		#[difference between each num in the seq.] or one parameter[num of ints to generate starting from 0];		#len() is a method w/ one parameter [seq. (string, bytes, tuple, list, or range) or
		#collection (dictionary, set, or frozen set)]
	for idx in range(iter_num):		#idx is any var name, range() is a method
		if listToSort[idx]>listToSort[idx+1]:	#comparison and swapping statements
			temp = listToSort[idx];
			listToSort[idx] = listToSort[idx+1];
			listToSort[idx+1] = temp;
print("List sorted, now printing:")
for num in listToSort:
	print(num);

	
	
# file I/O demo
fileObj = open("testFile.txt", "w+");	#file_object is a var name;	open() is a method w/ three parameters [file_name], [access_mode (like ifstream, ofstream, ios::in, ios::binary, etc.)], [buffering value]
		#access_mode is optional parameter. file_name and access_mode parameters must be strings
print("writing info to a file...");
fileObj.write("This is sample file I/O text.\n");	#write() is a method for outputting to file
print("writing complete. reading info from file and printing...");
print (fileObj.read());	#read() is a method w/ one optional parameter [<= this size bytes are read and returned] if end of file is reached read() returns empty string ('')
fileObj.close();	#close() is a method that flushes any unwritten info and closes the file obj. Python automatically closes a file when the ref obj of a file is reassigned to another file



# switch case equivalent	; there is no switch statement in Python, can be iplemented using dictionaries, functions, or classes
	# using dictionaries
	#define individual functions for each case
def first():
	return "Monday"
def second():
	return "Tuesday"
def third():
	return "Wednesday"
def default():		#write funct. for default case
	return "Invalid Day"
	# make dictionary obj. storing each funct.
switcher = {
	1: first,
	2: second,
	3: third
	}	#don't include default here
	#make switch() funct.
def switch(dayOfWeek):
	return switcher.get(dayOfWeek, default)();	#dictionaryName.get() method returns value w/ 
			#specified key in first arg., else returns value of second arg.
	#test switch case implementation
ctrl = 0;
while ctrl != 8:
	print("Enter a number between 1 and 3. Enter 8 to exit:");
	ctrl = int(input());
	print(switch(ctrl));
	
	# using classes
class pythonSwitch:	#pythonSwitch class defines switch() method
	def switch(self, dayOfWeek):
		default = "Invalid Day"
		return getattr(self, 'case_' + str(dayOfWeek), lambda:		#convert dayOfWeek arg
				#into string and append to 'case_' literal,	resulting string is
				#passed to getattr() method,	getattr() method returns a matching
				#funct. in the class,	if no match to string, returns lambda funct.
				#as default
	def case_1(self):	#define individual case funct.s here
		return "Monday"
	# don't define default case here
s = pythonSwitch()

print(s.switch(1))	
	
	
	
# function definition and call demo
def printSum(addend1, addend2):
	sum = addend1 + addend2;
	print(addend1 + " plus " + addend2 + " equals " (addend1 + addend2));
	return;
num1 = 5
num2 = 7
printSum(num1, num2);
	
	

# end of program message
print("===Program now ending, have a nice day.===");
