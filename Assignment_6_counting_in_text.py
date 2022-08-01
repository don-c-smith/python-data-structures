# In this assignment, we need to figure out and identify which person from the email text block has sent the most emails
# We need to read in the text and isolate the lines that start with 'From ' (NOT 'From:' with a colon)
# Then, we need to isolate the second word of each of those lines, which is an email address
# Then, we need to store each email address and the number of times it shows up in a dictionary
# Finally, we print the most common address and the number of times it occurs
# Output should be: cwen@iupui.edu 5
sender_list = list()  # Create an empty list called 'sender_list'
sender_dict = dict()  # Create an empty dictionary called 'sender_dict'
file_name = input('Enter file path:')  # We'll need to flip the slashes
text = open(file_name)  # Open the file, store it in 'text'
for line in text:
    if 'From:' in line:  # If the line contains 'From:'
        continue  # Skip it
    elif 'From' not in line:  # If the line doesn't contain 'From'
        continue  # Skip it
    else:  # Otherwise
        words = line.split()  # Extract these lines and split them into their component words
    for email_addresses in words:  # For each email address in the list of words
        email_addresses = words[1]  # The email address is the second word (index 1) of each line
    sender_list.append(email_addresses)  # Append each of those email addresses to the sender list
for sender in sender_list:  # For each sender in the list
    sender_dict[sender] = sender_dict.get(sender, 0) + 1  # Use get() to store the sender in the dictionary and count their occurrences
bigsender = None  # Start these variables with a 'None' value
sendcount = None  # Start these variables with a 'None' value
for k, v in sender_dict.items():  # For each key ('k') and value ('v') in the dictionary
    if sendcount is None or v > sendcount:  # Iterate through - if the value is higher than what's stored in sendcount
        bigsender = k  # Store that key value in the variable
        sendcount = v  # And its associated count in the other variable
print(bigsender, sendcount)  # Print the biggest sender and the number of emails they sent
