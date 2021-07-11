A set of useful python constructs I wrote (and keep updating)


	
	
	

	
	
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
