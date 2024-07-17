s = 'Monty Python'
# The range is up to, but not including, the last number. In [0:4], 4 is not included. We get M as 0, o as 1, n as 2, and t as 3. 
print(s[0:4])
print(s[6:7])
# The following is not a traceback because it is ok to reference beyond the end of a string in a range.
print(s[6:20])
# Blank in the following context represents zero
print(s[:2])
# Blank in the following context represents the end of the string
print(s[8:])
#In the following blank will represent zero and end of string
print(s[:])