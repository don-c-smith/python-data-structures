# In this assignment, we're given a long string with whitespace and told to extract the number at the end
# We need to return the number as a floating point datatype
# Output should be 0.8475
# We are supposed to do this using find() and string slicing
text = 'X-DSPAM-Confidence:    0.8475'  # Here's the original information
zero_pos = text.find('0')  # Find the index position of the zero
number_str = text[zero_pos:]  # Slice the string from the zero position to the end of the string
print(float(number_str))  # Print the float of the resulting sliced string
