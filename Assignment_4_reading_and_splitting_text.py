# In this assignment, we need to read in a block of Shakespeare, *line by line*
# For each line, we need to split the line into a list of its component words using split()
# This means the list will be "built" progressively with each line
# We are then supposed to check and see if each new word on each new line is already in the list
# If it isn't, we're supposed to append it to the list
# Finally, we're supposed to sort the list in alphabetical order
# The output is supposed to be:
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
file_name = input('Enter file name:')  # Note we'll need to flip the slashes beforehand
file = open(file_name)  # Open the file
word_list = list()  # Create an empty list called word_list
for word in file:  # For each word in the file
    word = word.rstrip()  # Trim off the white space on the right
    split_words = word.split()  # Split each line into its component words
    for individual_word in split_words:  # For each sequential word in the list of component words
        if individual_word not in word_list:  # If the currently-processed word is NOT in the empty list
            word_list.append(individual_word)  # Add it to the list
word_list.sort()  # Sort the list alphabetically
print(word_list)  # Print out the sorted list
# The key realization for this assignment was spotting the need for nested 'for' loops
# I needed one loop to split apart the initial lines, and another to read through each split-out word
