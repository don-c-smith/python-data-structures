# For the final exam,  we have to read in that big cloud of mailbox text
# We need to do the annoying user-input-slash-flip thing
# Then, as before, we need to isolate the lines starting with 'From' and NOT 'From:'
# Then, we need to split each of those lines (using a colon as the delimiter) to find the HOUR the email was sent
# Then, we need to count the number of emails grouped by hour sent and print our the frequencies by hour
# We'll be ordering by hour of the day in ascending order
# Final output should be:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
hour_list = list()  # Create an empty list to temporarily store the hour values
hour_dict = dict()  # Create an empty dictionary to store the hour values and their counts
file_path = input('Enter file path:')  # I need to flip the slashes
text = open(file_path)  # Open the file
for line in text:  # For each line in the file
    if 'From:' in line:  # If the line contains 'From:'
        continue  # Skip it
    elif 'From' not in line:  # If the line doesn't contain 'From'
        continue  # Skip it
    else:  # Otherwise
        first_pieces = line.split()  # Split the relevant lines into their component parts (words)
    for full_time in first_pieces:  # For each full time value in each line
        full_time = first_pieces[5]  # Extract the full time, which is at index position 5
    split_times = full_time.split(':')  # Split the full time values at the colons and create a list of the three values per line (hr/min/sec)
    for hour in split_times:  # For each hour value in the list of split-up times
        hour = split_times[0]  # Extract just the hour value, which is at index position 0
    hour_list.append(hour)  # And store each of those values in the hour list
for hour in hour_list:  # For each of those hour values in the hour list
    hour_dict[hour] = hour_dict.get(hour, 0) + 1  # Iterate, add to dictionary if absent, add 1 to frequency of that hour if already present
for k, v in sorted(hour_dict.items()):  # For each key-value pair in the dictionary, sort and...
    print(k, v)  # Print the key-value pairs in ascending order by hour
