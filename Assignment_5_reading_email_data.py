# For this assignment, we need to read in the big pile of email text from two assignments ago
# We then need to isolate each line that starts with 'From'
# We specifically do NOT want to include lines that start with 'From:' (lines with a colon after From)
# We then need to use split() to extract the person's email address, e.g. 'stephen.marquard@uct.ac.za'
# We then print out a duplicated list of those email addresses, followed by a count of the total number of relevant text lines
# The final count should read: There were 27 lines in the file with From as the first word
file_name = input('Enter file name:')  # We'll need to flip the slashes
file = open(file_name)  # Open the file
line_count = 0  # Here's our counting variable
for line in file:  # For each line in the file
    if 'From:' in line:  # If the line contains 'From:'
        continue  # Skip it
    elif 'From' not in line:  # If the line doesn't contain 'From'
        continue  # Skip it
    else:  # Otherwise
        pieces = line.split()  # Split the relevant lines into their component parts
    for email_address in pieces:  # For each email address among the pieces
        email_address = pieces[1]  # Set the value of email_address to the second 'piece' of each line
    print(email_address)  # Print each email address
    line_count = line_count + 1  # After you print each email address, add 1 to the counting variable
print('There were ' + str(line_count) + ' lines in the file with From as the first word')  # Print out the counting text
