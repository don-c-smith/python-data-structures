# This file contains code notes and examples of the Python concepts taught in level 2 of 'Python for Everybody'
# Level 2, 'Python Data Structures,' is about how to store, parse, and use data structures in Python
# These code examples show how to work with and execute the class' core concepts


# GOING IN-DEPTH WITH STRINGS
# The first thing we did in Python Data Structures was to learn more about how to work with string-type data
# This isn't exactly 'data structures' work but it's very important nonetheless

# THE 'LEN' FUNCTION AND STRINGS
# The len() function returns the number of characters in a string - its length
word = 'Peacock'  # This word has seven characters
print(len(word))  # Returns 7, the number of characters in the string

# 'UPPER' AND 'LOWER' WITH STRINGS
# The upper() and lower() functions are part of Python's string library
# You can append them to string-type variables ONLY
# These functions don't change the original string - they create modified copies of the original
name = 'Don Smith'  # Here's a 'proper case' name
lower_name = name.lower()  # This creates a new variable with the name as all lower-case letters
upper_name = name.upper() # This creates a new variable with the name as all lower-case letters
print(name)  # Returns the original "Don Smith"
print(lower_name)  # Returns "don smith"
print(upper_name)  # Returns "DON SMITH"

# 'REPLACE' WITH STRINGS
# The replace function replaces characters in a string with other characters
phrase = 'Hello, Wendy!'
new_phrase = phrase.replace('Wendy', 'Andy')  # Replace all occurrences of 'Wendy' with 'Andy
print(phrase)  # Returns 'Hello, Wendy!'
print(new_phrase)  # New phrase post-replace returns 'Hello, Andy!'

# INDEXING STRINGS
# You can use square brackets to find specific characters in strings. This is called "indexing."
# The index value can be a constant or a computed value.
# Note that the first character in a string is indexed at ZERO, not 1.
# We use the word "sub" to reference an indexing process - variable "sub" two would be x[2]
word = 'Peacock'
print(word[3])  # Note that this prints the FOURTH character in the string, not the third
# That's using a constant as an indexing value
x = 2
print(word[3 - x])  # This is using a calculation/expression as an indexing value
# Because x = 2, we're telling Python to print the second character - 3-2 = [1]

# 'FIND' WITH STRINGS
# You can use the find() function to search for specific characters or substrings in strings
# The return will be the position of the character/substring or -1 if it isn't found
word = 'Peacock'
pos_ock = word.find('ock')  # Find the substring 'ock' in the word
print(pos_ock)  # Print its position which is 4 - 'o' is the fifth letter of the string (Remember [0] comes first!)
pos_zz = word.find('zz')  # Find the substring 'zz' in the word
print(pos_zz)  # This substring doesn't exist in the word so the return is -1 - "Not found"

# FINDING SUBSTRINGS IN STRINGS
# The 'in' keyword can also be used as a logical operator to search for characters or substrings
word = 'Peacock'
if 'e' in word:
    print('Found')
else:
    print('Not found')
# Returns 'Found'

if 'Pea' in word:
    print('Found')
else:
    print('Not found')
# Returns 'Found'

if 'Squid' in word:
    print('Found')
else:
    print('Not found')
# Returns 'Not found'

# You can use combinations of string functions to extract a specified substring from a longer string
# For example, let's say you had a long string of an email sender and you wanted to know the sender's domain
data = 'From: Sherry Mooney <sharon.j.mooney@gmail.com> 6/27/22 - 4:27:43 PM CDT'  # Here's the whole string info
# We just want to know which email address Sherry sent this email from
atpos = data.find('@')  # Find the index position of the '@' sign and store it in this variable
closepos = data.find('>', atpos)  # Find the index position of the '>' character, starting the search at the atpos value
domain = data[atpos+1:closepos]  # The domain is what starts right AFTER the '@' until right BEFORE the '>'
print(domain)  # And we get the domain

# 'SLICING' STRINGS
# You can use square brackets with specific numbers and colons to grab "slices" of a string
# The second number provided after the colon is one MORE than the slice - "up to but not including"
word = 'Peacock'
print(word[0:2])  # This will print the first TWO characters of the string - 'Pe'. See comment in line 2
print(word[1:5])  # This will print the second through the fourth characters - 'eaco'
print(word[3:50])  # If the second number you provide is longer than the string, it stops at the end of the string
print(word[:3])  # If you put nothing in front of the colon, Python assumes you mean the start of the string
print(word[2:])  # If you put nothing after the colon, Python assumes you mean the end of the string
print(word[:])  # If you supply no values, Python prints the whole string

# STRIPPING WHITESPACE FROM STRINGS
# There are also functions to remove whitespace from strings.
# lstrip() removes whitespace from the left of a string, rstrip() from the right, strip() from both ends
word = '     Don      '  # This string has whitespace on both ends
left_word = word.lstrip()
right_word = word.rstrip()
full_word = word.strip()
print(word)  # Returns 'Don' with all spaces
print(left_word)  # Returns only right-hand spaces after 'Don'
print(right_word)  # Returns only left-hand spaces after 'Don'
print(full_word)  # Returns 'Don' with no spaces

# THE 'NEWLINE' CHARACTER
# The newline character is how you indicate to Python that a line-break exists/should exist.
# In strings, it's '\n'. Internally in Python it counts as one character, not two
declare = 'I am Don'  # Here's a string with no newline character
declare_newline = 'I am \nDon'  # Here's a string with a newline character
print(declare)
print(declare_newline)  # Note that this string prints with a line break
print(len(declare))  # Returns 8 characters - 6 letters, 2 spaces
print(len(declare_newline))  # Returns *9* characters - 6 letters, 2 spaces, *1* newline character

# COUNTING OCCURRENCES IN STRINGS
# You can use a loop to count the number of times a given character appears in a string
word = 'Peacock'  # Here's our string
letter_count = 0  # Here's our counting variable, which starts at zero as usual
for character in word:  # For each character in the word
    if character == 'c':  # If the character being processed is a c
        letter_count = letter_count + 1  # Add 1 to the counting variable
print(letter_count)  # Print the number of 'c's in the word, which is 2

# USING INDEFINITE LOOPS WITH STRINGS
# You can use a 'while' loop along with indexing and the len() function to loop through a string
word = 'Peacock'  # Start by storing a string in the variable
index = 0  # Start the indexing variable at 0, which is the beginning of the string
while index < len(word):  # As long as the value of indexing variable is less than the numerical length of the string
    character = word[index]  # The new variable, which is each character, is equal to the current index value of the string variable
    print(index, character)
    index = index + 1  # After each character is processed, add 1 to the indexing variable to advance to the next character
# The result is each indexing value accompanied by each associated character in the string

# USING DEFINITE LOOPS WITH STRINGS
# If you don't care about indexing and character position, you can also loop through a string using a 'for' loop
# This 'definite' loop will run through the string until it runs out of characters
word = 'Peacock'  # Start by assigning a string to a variable
for character in word:  # For each character in the string variable
    print(character)  # Print each letter until the characters run out


# OUR FIRST DATA STRUCTURE: LISTS

# Lists are data structures that contain multiple values, or 'elements'
# They can contain string, numbers, and even other lists. They can also be empty
# Lists are bound by square brackets and their elements are separated by commas
# Lists have indexes - list[2] will return the THIRD element in a list
# Lists are "mutable" - they can be changed in ways that strings can't
boys = ['Don', 'Mike', 'Joe', 'Bart', 'Steve']  # Here is a list with three guys' names
print(boys)  # This will print the list contents, including the commas and brackets
print(boys[2])  # This prints the THIRD element in the list: "Joe"
# You can use the len() function to tell you how many elements are in a list
print(len(boys))  # This returns 5 - there are five names in the list
# Let's say Bart wanted to be called 'Andrew' in the list, instead
boys[3] = 'Andrew'  # This changes the value of the fourth element in the list (index 3) to Andrew
print(boys)  # Now the fourth name is 'Andrew'
# You can also create a new list by adding two lists together.
girls = ['Maggie', 'Lucy', 'Wynn', 'Crissy', 'Madeline']  # Here's a list of five girls
print(boys)  # Here's the list of boys
print(girls)  # Here's the list of girls
CHASS = boys + girls  # You can just use a plus sign to combine lists - basically "concatenate"
print(CHASS)  # And here's the new, combined list
# You can also use index values to extract or print 'slices' of a list
print(CHASS[0:5])  # This gives us just the boys - note that we use index 5 for "up to but NOT including"
mid_list = CHASS[4:8]  # This creates a new list containing names/elements 4 through 7 of the full list
print(mid_list)  # Here's the extracted sub-list

# APPENDING VALUES TO LISTS
# You can use the built-in append() function to add values to lists
boys = list()  # This creates an empty list called 'boys'
print(boys)  # If you print it, it's empty
boys.append('Don')  # Let's add me to the list
print(boys)  # Now, I'm in the list!
# Note that append() adds new values to the END of the list
# append() does actually *change* the list - it's not 'creating a copy'

# SORTING LISTS
# The elements in lists can be sorted
# However, be aware that doing so will change the order of the list! It's a 'modify,' not an 'alias'
numbers = [1, 3, 2, 5, 6]  # Here's a list of numbers
print(numbers)  # As you can see, it's out of order and missing a 4
numbers.sort()  # Sorting the list in ascending order
print(numbers)  # Now the list is ordered, but persistently changed
numbers.append(4)  # This will add a 4 to the list
print(numbers)  # But because we used append(), the 4 is at the end of the list
numbers.sort()  # If we sort again...
print(numbers)  # Everything is as it should be
# You can also use max(), min(), and sum() with lists if you pass the list name as the function's parameter
print(max(numbers))  # Returns 6
print(min(numbers))  # Returns 1
print(sum(numbers))  # Returns 21

# SPLITTING STRINGS INTO LISTS
# The split() functions breaks apart a string into its component parts and stores those parts (usually words) in a list
phrase = 'These three words'  # Initial string
word_list = phrase.split()  # Splitting the component parts at the spaces into a list
print(phrase)  # Here's the whole phrase
print(word_list)  # Here's the list that the split() function created
print(len(word_list))  # Returns 3 - there are three elements (words) in the list
print(word_list[1])  # Prints "three" - the second word (first index position) in the list
for word in word_list:  # For each word in the list
    print(word)  # Print each word in order
# This is a CRUCIAL process - it's how we look through individual words in a long text string and find/change things
# Another important process is the "double-split," through which you split extracted pieces into smaller pieces
# Let's use the email text line example again
# If we wanted to find just the domain, using a double-split makes everything easier because you don't need 'atpos' etc.
text = 'From: Sherry Mooney <sharon.j.mooney@gmail.com> 6/29/2022 2:48:27 PM'
print(text)  # This is a mess - we just want the domain
clean_text = text.replace('>', ' ')  # New string, dropping the closing '>' character after the email address
pieces = clean_text.split()  # Splitting on the whitespace character
print(pieces)  # Checking the split process
email = pieces[3]  # Extracting just the email address at index 3
print(email)  # Checking the extraction process
domain = email.split('@')  # Splitting at the '@' sign
print(domain[1])  # Printing the second piece, everything after the '@' sign at index position 1

# USING ITERATION WITH LISTS
# Lists can also be created and operated upon through iteration. This is a development of things we did earlier
# Let's take the example of adding up a list of numbers and calculating the average of the numbers we end up entering
# First, let's do it without a list, using counting and running sum variables
total = 0  # Starting with our numerical total at zero
count = 0  # And with our count at zero
while True:  # An indefinite loop
    inp = input('Enter a number:')  # Asking for a number
    if inp == 'Done':  # Here's our 'exit ramp'
        break  # If the user types 'Done', the process stops
    value = float(inp)  # Turn the string number into a float
    total = total + value  # Add it to the running sum
    count = count + 1  # Increase the count of values at each entry by one
average = total/count  # Compute the average
print(average)  # Print the average
# Now, using a list
numbers = list()  # Starting with an empty list
while True:  # Another indefinite loop
    inp = input('Enter a number:')  # Asking for the number
    if inp == 'Done':  # Exit ramp
        break
    value = float(inp)  # Float conversion
    numbers.append(value)  # Now we're appending each value, i.e. adding it into the list
average = sum(numbers)/len(numbers)  # Using list operators to compute an average
print(average)  # Printing the average
# If you enter the same values, you'll get the exact same results from both processes
# The point is that using lists is a little smoother and more comprehensible
# One thing worth mentioning is that method one only handles one number at a time because it recomputes a running sum
# The second method stores ALL the numbers in a list in memory BEFORE it computes an average
# So, if you're working with a HUGE list of numbers, method 1 will be much more resource-efficient


# OPENING FILES IN PYTHON
# Obviously, knowing how to open and access files is crucial for any useful programming to occur
# Using the open() function to access and create a "handle" for a file
# Supply the filepath as a string - you will need to invert the direction of the slashes because Windows
# After the comma, supply a mode - "r" for reading the file and "w" for writing to it
# You can also get a user to input a file name using input(), which passes a string.
file = open('C:/Users/doncs/Documents/Python Data Structures/mbox.txt', 'r')
print(file)
# We can also use a 'for' loop to iterate through the lines in the file since it's a sequence - an ordered set
# So, for example, we could count the lines in a file
line_count = 0  # Starting off with our counter variable set to zero
for line in file:  # For each line in the file
    line_count = line_count + 1  # Add 1 to the line count
print(line_count)  # Print the final line count

# You can search for specific text/characters within a file using a 'for' loop
text_file = open("C:/Users/doncs/Documents/Python Data Structures/mbox.txt")  # Start by opening the file
print(text_file)
for line in text_file:  # For each line in the file
    if line.startswith('From: '):  # If the line starts with 'From: '
        print(line)  # Print that line
# However, you'll notice that if you print it that way, the output is full of blank lines
# That's because the print() function by default is adding new lines during iteration
# So, we're "doubling up" - the print function is adding a \n to the \n already in the text file. Not good.
# We can deal with this by using the rstrip() function to remove the newline characters from the text file
for newline in text_file:
    newline = newline.rstrip()
    if newline.startswith('From:'):
        print(newline)

# You can also select and print specific lines based on their content
file = open("C:/Users/doncs/Documents/Python Data Structures/mbox.txt")  # Start by opening the file
for line in file:  # For each line in the file
    line = line.rstrip()  # Strip the rightmost whitespace (built-in newline character)
    if '@uct.ac.za' not in line:  # If this specific text string is NOT in the line
        continue  # Skip that line and return to the top of the loop
    print(line)  # Print all the lines containing that string


# OUR SECOND DATA STRUCTURE: DICTIONARIES

# Dictionaries are another 'collection' like lists, meaning they contain multiple values.
# However, unlike lists, which have a strict indexed order, dictionaries are unordered 'bags' of data
# In a dictionary, each value has an associated 'key.' It's a value-pair structure. Also called an 'associative array'
don_info = dict()  # This will create an empty dictionary
don_info['Name'] = 'Don'  # This inserts the value 'Don' with the key 'Name'
don_info['Age'] = 35  # This inserts the value 35 with the key 'Age'
don_info['FavColor'] = 'Green'  # This inserts the value 'Green' with the key 'FavColor'
print(don_info)  # Returns {'Name': 'Don', 'Age': 35, 'FavColor': 'Green'}
# You can also change the values stored in dictionaries by referencing their keys
# Let's say I wanted to change my favorite color to 'Dark Green'
don_info['FavColor'] = 'Dark Green'  # Here's the change to an existing dictionary
print(don_info)  # Updated: returns {'Name': 'Don', 'Age': 35, 'FavColor': 'Dark Green'}
# You can also print specific values in the dictionary by calling their associated key.
print(don_info['Name'])  # This returns 'Don'

# You can also create and add values to dictionaries in a single 'literal' step.
# NOTE: Here's our first use of 'curly' brackets.
sherry_info = {'Name': 'Sherry', 'Age': 35, 'FavColor': 'Blue'}  # Creates a dictionary AND fills the values and keys
print(sherry_info)  # This prints the dictionary. Same structure/output type as before, just created all at once
# You can print just the keys from a dictionary:
print(sherry_info.keys())
# Or just the values:
print(sherry_info.values())
# Or both, the "items":
print(sherry_info.items())

# COUNTING WITH DICTIONARIES
# One common use of dictionaries is a counting-related process.
# We use the categories or 'bins' as the keys and the number of observances as the associated values
# For example, polling people for their favorite color.
color_pop = {'Red': 0, 'Blue': 0, 'Green': 0, 'Yellow': 0}  # Building a dictionary with four colors and zero counts
print(color_pop)  # As expected, each color is present with an associated value of zero.
color_pop['Red'] = color_pop['Red'] + 1  # We got our first response of 'Red' as a favorite color
print(color_pop)  # Now the 'Red' Key has an associated value of 1.
# Let's poll four more people.
color_pop['Red'] = color_pop['Red'] + 1  # Another person says 'Red'
color_pop['Blue'] = color_pop['Blue'] + 1  # Someone says 'Blue'
color_pop['Green'] = color_pop['Green'] + 1  # Someone says 'Green'
color_pop['Blue'] = color_pop['Blue'] + 1  # The last person polled says 'Blue'
print(color_pop)  # Returns the results of the five respondents: {'Red': 2, 'Blue': 2, 'Green': 1, 'Yellow': 0}
# This is an example of a dictionary 'growing' given repeated inputs
# Doing this kind of thing through iteration is common and useful in data science for obvious reasons
# You can also check the value associated with a specific key in this dictionary:
print(color_pop['Blue'])  # Returns 2
# If you try to call a key that isn't in the dictionary, you get a traceback error:
# print(color_pop['Orange'])  # This triggers an error. There is no key called 'Orange' in the dictionary
# You can use the 'in' keyword to check if a given key is in a dictionary.
print('Red' in color_pop)  # Returns True
print('Orange' in color_pop)  # Returns False

# USING 'GET' WITH DICTIONARIES
# You can search a dictionary to see if a key is present and reurning a default value (rather than a traceback error) if it isn't
# It's common enough that there's a built-in Python function that helps you do it called get()
# Let's build a tiny dictionary to start
sherry_info = {'Name': 'Sherry', 'Age': 35, 'FavColor': 'Blue'}  # Creates a dictionary AND fills the values and keys
# Now let's check to see if this info dictionary has a value for 'Name':
print(sherry_info.get('Name', 'ABSENT'))  # Returns 'Sherry.' The 'Name' key WAS present, and this is its associated value
# The 'ABSENT' string appearing after the comma is the default value that will be returned if the key ISN'T present
print(sherry_info.get('Weight', 'ABSENT'))  # Returns 'ABSENT' - there is no key value called 'Weight'
# The key point here is that the get() method will prevent you from getting traceback errors

# ITERATING ADDITIONS TO DICTIONARIES
# You can use conditional logic and iteration to intelligently add things to dictionaries
# For example, feeding a *list* of last names into a dictionary, adding a new name when it comes up, counting frequencies of existing names
name_count = dict()  # Creating an empty dictionary called 'name_count'
last_names = ['Jones', 'Smith', 'Johnson', 'Smith', 'Smith', 'Jones', 'Carson', 'Rosen', 'Johnson', 'Bohr']
for name in last_names:  # For each of the names in the list of last names
    if name not in name_count:  # If the name being processed is not in the dictionary
        name_count[name] = 1  # Add that name as a key value and assign it a value of 1
    else:  # Otherwise, if it's already in the dictionary:
        name_count[name] = name_count[name] + 1  # Add 1 to its associated value
print(name_count)  # Returns {'Jones': 2, 'Smith': 3, 'Johnson': 2, 'Carson': 1, 'Rosen': 1, 'Bohr': 1}
# This is each name in the list with the associated number of times it occurred in the list

# 'DYNAMIC' LIST/DICTIONARY INTERACTIONS - "LIST COMPREHENSION"
# You can use Python's ability to comprehend dynamic lists to cut down on the amount of code you have to write
# You can put iteration commands inside of lists! Not everything has to be static
# Let's start with a simple dictionary:
dict = {'a':5, 'c': 15, 'b':40}
print(dict)  # Prints as expected
print(sorted(dict.items()))  # Now we have a dictionary sorted by KEY
# If we want to sort by value, we CAN do what we've done before:
templist = list()  # Create a blank list
for k,v in dict.items():  # For each key-value pair in the items() call of the dictionary
    fliptuple = templist.append( (v,k) )  # Create the value-key pairs and drop them into a temporary list
templist = sorted(templist, reverse=True)  # Sort this new list in descending order by value
print(templist)  # Prints as a single line
for k,v in templist:
    print(v,k)  # Prints line-by-line
# That works. That's totally fine
# But there's a better way, using Python's ability for 'list comprehension'
print(dict)  # There's the dictionary again
# In a single line of code, we can call sorted() and items() and 'for' and print a descending-order list sorted by VALUES
print(sorted([(v, k) for k, v in dict.items()], reverse=True))
# Okay, so, let's walk through that. We are saying:
# 1. For each flipped tuple (v.k)
# 2. Of each key-value pair k,v
# 3. In the items() call off the dictionary
# 4. Sort said flipped tuples in reverse order - sorted(...,reverse=True)
# 5. And print the resultant list


# OUR THIRD AND FINAL DATA STRUCTURE: TUPLES

# Tuples are the third data structure we're learning. They are very similar to lists except they can't be modified
# They are more memory-efficient than lists because Python knows the contents of tuples will never change
# Remember that the items() function applied to dictionaries will return a list of tuples: the k-v pairs
# They do have several cool uses
# You assign a tuple with regular parentheses and commas separating the values
tuple = (2, 4, 6, 8)
print(tuple)  # Looks like a list with parentheses instead of square brackets
# You can't sort dictionaries, but you CAN sort the items()-based list of tuples. This allows you to *functionally* sort a dictionary.
# Here's a dictionary with a weird order:
dict = {'a':5, 'c':15, 'b':40}
print(dict)  # You can see that the dictionary is 'out of order' both in terms of keys and values
print(dict.items())  # Now you can see the tuples making up the dictionary. By sorting these tuples, we can create a sorted copy of the dictionary.
# We do this using the sorted() function. Sorting by keys is easy, because you can't have duplicate keys in dictionaries.
print(sorted(dict.items()))  # Now it's in key order, alphabetically.
# You can also use a for loop to iterate through the items (tuples) in a dictionary and print them in a sorted order
for k,v in sorted(dict.items()):  # for each key and value in the sorted version of the dictionary:
    print(k,v)  # Print the ordered/sorted key-value pairs. Now each pair is ordered BY KEY and has its own line
# Sorting by value is trickier.
# Essentially what you do is flip the values in the tuples - creating a new "flipped" LIST of tuples that's value-key instead of key-value.
# You do this by iterating through the tuples in the dictionary with a for loop
newdict = {'a':5, 'c':15, 'b':40}  # Here's a new dictionary
templist = list()  # Here's an empty, temporary-use list
print(newdict.items())  # The dictionary prints as expected
for k,v in newdict.items():  # For each key-value pair in the dictionary
    templist.append( (v, k) )  # Append tuples to the new empty list in VALUE-KEY order. **Note the need for parentheses, as we can only create one element at a time in the new list**
print(templist)  # Now the list has the dictionary's key-value pairs stored as tuples in VALUE-KEY order
# Now we can sort that list of tuples
templist = sorted(templist, reverse=True)  # For kicks, we'll sort by values in descending order, hence the reverse
print(templist)  # Returns [(40, 'b'), (15, 'c'), (5, 'a')]

# USING TUPLES WITH OTHER DATA STRUCTURES
# Let's build a program that uses the interactions of tuples, lists, and dictionaries
# We'll analyze some text and print out not the most-common word and it's frequency, but the sorted TEN most-common words
# We'll need a temporary list and a dictionary
templist = list()  # There's our empty list
dict = dict()  # There's our empty dictionary
text = open('C:/Users/doncs/Documents/Python Data Structures/romeo.txt')  # Open the file
for line in text:  # For each line in the text
    individual_words = line.split()  # Split up the lines into words and store them in a list called 'individual_words'
    for word in individual_words:  # For each word in that list of words
        dict[word] = dict.get(word, 0) + 1  # Here's the count-up use of the get() function with the dictionary
for k, v in dict.items():  # For each key and value in the tuple-based item() call in the dictionary
    fliptuple = templist.append( (v,k))  # Create a new item, which is a 'flipped' tuple in value-key format, and append it to the list
templist = sorted(templist, reverse=True)  # Sort this new list in descending order by value
for v, k in templist[:10]:  # For the top ten highest values (note the [:10] list slicing) in the sorted list:
    print(k, v)  # Print the word (key) and its frequency of occurrence (value)

