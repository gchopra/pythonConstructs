A set of useful python constructs I wrote (and keep updating)


Interpretation:
Python has top to bottom interpretation -- hence function must be defined before it is used.
Recommended that all function definitions are put at the top

Operation on numbers:
Division will always result in a float response in python operations
	Quotient -> // 
	Remainder -> %
	Exponent -> **  Example : 3**4 is 81
For other operations you need to import from the math library:
	From math import *
	This would give you functions like log(), sqrt(), sin() ..
Names have a special feature in python -- they can be assigned values of different types as the program evolves. Hence, names don't have a fixed type
	
![image](https://user-images.githubusercontent.com/30420102/125206858-edce9f80-e24e-11eb-9890-0009c676152a.png)

Type(e) gives type of an expression e
Boolean values: they are True or False
	


String type:
Str is a sequence of characters
A double quote can include single quote " ' " but single quote can't include unless you have a backslash in the middle ' \' '
A triple quote can include double and single quotes without backslash ''' '  " '''
	

"+" is used to concatenate strings
Len() operator gives the length of string
	

Strings are immutable -- hence modifications are tricky:
	


Lists:
Can be numbers, strings or mixed also.
Extraction of values by position (slicing) possible like strings
len() gives number of elements in the list

	

Nested lists exist too:
	

Unlike strings, lists can be updated in place -- hence they are mutable
To copy lists -- always use a full slice, because otherwise it creates pointer to the list instead of a new list:
	

In case there is an equality check needed for things pointing to same object -- we use "is"
	

Concatenation is done using "+" for lists -- and it produces a new list

Control Flow
Indentation is key:
	

For conditional checks:
	

Nested "if" -- use "elif"
"Else" is always optional 

Loops
We use range to specify the sequence of values to go through in the loop
	Range(0,n) gives us 0, 1, …. ,n-1
	Range(I,j) gives us I, I+1, … j-1
Conditional looping: While <condition>
Break is used to exit from a loop
"else:" clause: If you go through a for loop with break statement in it… and break doesn’t happen(i.e. normal termination), you can choose to have an "else:" part to the loop as special action for normal termination

Functions
It can be called a unit of computation that is used time to time
def <function name>(<parameters>)
In value passing to functions, if the object is mutable, then the original value is changed, if immutable--value remains unchanged
Names within a function have local scope
Define functions before using them:
	

A function can call itself -- it's called recursion

More about range()
Range(I,j) gives sequence : i, i+1, …, j-1
Range(j) gives sequence : 0, 1, … j-1
Range(I, j, k) gives sequence: I, i+k, …. i+nk -- this stops before i+nk crosses j (that is -- i+nk < j)
Range is a list in Python2 but not in Python3
You can still do a type conversion to list : list(range(0,5))


List manipulation
Concatenation produces a new list (using the "+" operator)
Extending a list : list1.append(12) -- append happens in-place hence it's not a new list
Appending list: list1.extend(list2) -- same as -- list1 = list1+list2
Removing: list1.remove(x) -- removes first occurrence of x
List membership: x in list1 -- this returns true if x is found in list1 
Some other functions in list manipulation:
	l.reverse()
	l.sort() -- sort in ascending order
	l.index(x) -- leftmost position of x
	l.rindex(x) -- rightmost position of x
Before the first append you need to initialize the variable as a list --- "list1 = []"


Arrays compared with Lists
Arrays -- contiguous memory blocks
	Constant time -- Arrays have faster indexing (constant time for arr[i] regardless of value if "i")
	Linear time -- Insertion and contraction is expensive in an array, as values need to be shifted down or up respectively
Lists --- values ae scattered in memory. Each element points to the next
	In lists each element can have a different type as the memory space is not fixed -- hence flexible size
	Linear time -- Lists have a cost to indexing -- proportional to i for seq[i]
	Constant time -- List Insertion and deletion is easy -- just break a link and point again


Efficiency of Algorithms
We go for worst case behavior to report efficiency
Time complexity deals with finding out how the computational time of an algorithm changes with the change in size of the input.
Space complexity deals with finding out how much (extra)space would be required by the algorithm with change in the input size.
For Binary search algorithm efficiency:
	

Binary searching in:
	Unsorted array -- takes O(n)
	Sorted array -- takes O(log n)
	


Selection sort -- takes O(n2)
	

Insertion sort -- takes O(n2)
	

Recursion:
	Inductive definitions give rise to recursive programs
	There is a recursion limit(997) that can be raised manually -- sys.raiserecursionlimit(<your value>)
	

MergeSort:
	This is better than selection sort & insertion sort
	Divide and conquer strategy
	Divide the list into two parts recursively, then merge after sorting them
	takes O(n log n)
	
Quicksort:
	Choose a pivot element, and partition into lower and upper parts -- then recursively partition the two partitions
	Worst case is --- if pivot is max or min -- or it's an already sorted array -- takes O(n2)
	But the average case is -- O(n log n)
	In practice this is the fastest -- used the most
	
	
Tuples and dictionaries
Tuples
	Tuples allow simultaneous assignments
	A tuple can also be assigned to a name: 
		point = (3.5, 4.5)
	Initialization "()" : Tes1 = ()
	Tuples are immutable
	
Dictionary
	It's like a list with any arbitrary index as the key
	Example:
		Test1["abc"] = 11
		Test1["def"] = 44
	They are mutable like lists
	Initialization of dictionary is "{}" and not  "[]" : Tes1 = {}
	Nested dictionaries with multiple levels of keys possible:
	
	
	d.keys returns sequence of keys in dictionary d:
		for k in d.keys():
		   <do stuff>
	

Function definitions
Value can be passed by name:
	Power(n=5,x=4)
Functions can have default arguments:
	Example int has:  int(s,b)  --> b by default is 10
	Int("A5") is an error
	Int("A5", 16) is 165
Can assign a function to a new name:
	Def f(a,b,c):
	   ……..
	g=f
	Thus g becomes another name for f
Functions can be passed to other functions as arguments:
	

	
	
	
Map() & filter() functions
Map applies a function each element of a list : map(f, l) --- output is not a list you need conversion --- list(map(f, l))
Filter checks a property p for each element of a list l -- output is a sub-list -- filter(p, l)
	

Another way of generating such numbers is as follows: *here z cycles first-then x-then y
	


Exception Handling
The errors that are predictable are called exceptions 
Un-tapped exceptions result in program exiting abnormally

	
	

	
	
When dealing with files and input/output -- we use exception handling often
An example of exception handling:
	
	
Input and Output
Printing on screen:
	Reading from keyboard -- number = input("Enter a number: ")
	Print on screen -- print ("x:",x,"y:",y)
	Sep="…" and end="…" --- arguments that specify what should separate the output strings on the screen
	Format() used in positional printing -- "first {a}, second {b}".format(a=11,b=12)
File handling
	fhandle = open("<file name>", "<mode r, w or a>")
	Opening a file creates a file handle -- which is like a buffer
	Read and write are to the handle
	Closing handle == flushing it to disk
	Result = fhandle.read() --> reads entire file as a single string
	Result = fhandle.readline() --> reads one line
	Result = fhandle.readlines() --> reads entire file as list of strings
	Fhandle.seek(n) --> moves to position n
	Fhandle.read(n) --> reads first n characters
	End Of File : if fhandle.read() or fhandle.readline() return empty string ""
	Fhandle.write(s) --> writes string s to file and returns number of characters written
	Fhandle.writelines(l) --> write a list of lines l to file
	Fhandle.close() --> flushes and decouples the file handle
	Fhandle.flush() --> flushes without closing
	Stripping '\n':
		For line in fhandle.readlines():
			S = line[:-1]
	Stripping whitespaces and '\n':
		For line in fhandle.readlines():
			S = line.rstrip()
	Strip() --> both sides stripped
	Lstrip() --> strip from left
String functions:
	s.find(pattern) --> returns first pos in s where pattern occurs, returns -1 if  not found
	s.find(pattern, start, end) --> find in slice s[start : end]
	s.index(pattern), s.index(pattern,start,end) --> like find but raise ValueError if pattern not found
	s.replace(astr,bstr) --> replaces each astr to bstr
	s.replace(astr,bstr,n) --> replace at most n copies
	s.split(",") --> split into chunks between commas
	s.split(",",n) --> split into n chunks at-most
	Joinstring.join(columns) --> joins strings with joinstring="," …etc
	s.capitalize() s.lower()  s.upper() etc…
	s.center(n) --> string of length n with s in center
	s.center(n,"*") --> fill with * instead of blanks
	s.ljust() s.rjust() --> same with left or right justify
	s.isalpha() s.isnumeric() --> nature of characters in string
Misc. functions
	Pass --> a do nothing statement
	Del() --> contracts the lists and dictionaries and shifts elements, also can un-define a value
	None is assigned to initialize a name .. And later assign a value

Global scope
To make immutable value accessible globally, use the "global" keyword to define it in a function
Mutable values can be used globally by default
If u update immutable -- it creates a local copy


	
Data Structures
Arrays and list -- (sequences of values)
Dictionaries -- key-value pairs
Sets:
	Essentially a list with no duplicates
	Create an empty set -- colors = set() 
		**Because colors = {} is empty dictionary
	Converting list to set:
		
	Sets support operations like:
		Union -- set1 | set2
		Intersection -- set1 & set2
		Set -- difference set1-set2
		Xor --  set1 ^ set2
Stacks:
	Stack is a LIFO list
	Good at keeping track of recursive function calls
	Functions:
		s.append(x) -- add x to stack s
		s.pop() -- returns last element added
Queues
	FIFO sequence
	Useful for breadth first explorations
	Addq(q,x) -- adds x to rear of queue
	Removeq(q) -- removes element at head of queue

Heaps:


Hash Tables:
Use only if you don’t care about the data being sorted
We first use a hash function which returns a non-negative integer
Then we store the data in array element represented by hash-code


Use a good hash function pre-written as Writing your own hash function is the efficient.

Using hash function might result in the problem of collision where 2 data units result in same hash code. In such cases you can do a +1 search, but even that is limited & causes clustering. 
The real solution is chaining. We use linked list at each key location:







Abstract Datatypes:
You can go beyond built-in data types and create your own
If you abstract the datatype -- the implementation can be optimized without affecting functionality
Class is a template and object is a concrete instance of that template to which u can apply its defined functions
Constructor: ___init__(self,x):
	Self refers to the object you are operating on, which here refers to itself
	__init__ is a constructor which creates an object of the class with the name given
	You can have default argument values in __init__() too -- to initialize values in case object definer doesn’t define
Other special functions classes have:
	__str__() -- to print the contents of an object -- invoked by print()
	__add__() -- invoked by "+" -- 
		
	
	__mult__() -- called by "*"
	__lt__(), __gt__(), __le__() -- invoked by < , >, <= etc…
	

Binary Search tree and AVL tree
	BST: for each node -- value on left us less and value on right is more than current node
	AVL -- tree balancing mechanism
	
Memoization
This tries to make inductive definitions more efficient than naïve recursions
Store each computed value in a table --- look up the table before starting a recursive computation
	
Dynamic programming : predict the memory table and solve the sub problems in order of dependencies



Python vs other languages

Python has dynamic allocation of space
You can deallocate storage using del(x)
Garbage collection is automated in Python and Java -- hence reclaim space

Pros:
	No name declaration in advance
	No explicit memory management
	Garbage collection
Cons:
	Mistyped names sometimes as we don't declare them
	Need object creation to associate a name with a  type
	No private public declarations
	
	
	
	

Sorting Algorithms:

Insertion sort
Selection sort
Bubble sort
Merge sort
Quick sort
Heap sort
Shell Sort





Binary Tree:

Complete Tree: 
Every level is filled except last
All nodes in the last level are as far left as possible


Full Tree:
Every node has 0 or 2 children



Binary Tree traversal: It is the process of traversing each node in a tree exactly once
2 ways to traverse: Depth first and Breadth first

DFS methods:

Pre order traversal: root node -> left node -> right node 
Post order traversal: left node -> root node -> right node
In order traversal: left node -> right node -> root node



Binary Search Tree:
The property to be satisfied is:
The node on the left is smaller than current node
The node on the  right is greater than current node 





![image](https://user-images.githubusercontent.com/30420102/125206839-d1326780-e24e-11eb-9783-e15418b947fc.png)
