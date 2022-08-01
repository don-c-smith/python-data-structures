# In this assignment, we have to parse a text file, extract lines of interest that contain numbers, and run calculations
# We have to get the file name via input(), then open the file, and look for lines that start with 'X-DSPAM-Confidence:'
# We have to isolate those lines and extract the floating point values from each one
# We then have to count the lines and run an average of those floating point values
# The desired output is Average spam confidence: 0.7507185185185187
file_name = input('Enter file path:')  # Get the file path from the user
file = open(file_name, 'r')  # Open the file/activate the 'handle'
line_count = 0  # We'll need this for the average calculation, setting to zero to start
float_total = 0  # Since we can't use the sum() function, we need to do a running sum
for line in file:  # For each line in the file
    if not line.startswith('X-DSPAM-Confidence:'):  # If the line does NOT start with this string
        continue  # Skip it and iterate again
    line = line.rstrip()  # Take all unskipped lines and strip the whitespace from the right
    zeropos = line.find('0')  # Find the position of the zero in each selected line
    number_extract = line[zeropos:]  # Extract just the numerical characters by going from the zero to the end
    float_extract = float(number_extract)  # That's still a string, convert it to float
    float_total = float_total + float_extract  # Add each extracted float value per line to the float total
    line_count = line_count + 1  # Add 1 to the line count for each selected line
float_avg = float_total/line_count  # Step outside the loop and calculate an average
print('Average spam confidence:', float_avg)  # Produce desired output
