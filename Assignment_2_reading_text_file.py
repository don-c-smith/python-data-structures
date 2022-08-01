# In this assignment, we are required to read in a provided text file, reads through the file, and prints each line
# They don't want extra line breaks and also want us to convert the text to all uppercase
file = open('C:/Users/doncs/Documents/Python Data Structures/words.txt', 'r')  # Open the file as read-only
for line in file:
    clean_line = line.strip()  # Remove spaces on end of lines to avoid "doubling up" with print()
    caps_line = clean_line.upper()  # Capitalize all characters
    print(caps_line)  # Print the stripped, capitalized lines
