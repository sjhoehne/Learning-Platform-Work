#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
first_number = text.find('0')
last_number = text.find('5')
whole = float(text[first_number:last_number+1])
print(whole)