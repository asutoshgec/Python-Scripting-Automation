'''#Strip
y = "python"
print(y)

#If unwantedly I have given multiple spaces at the left side or right side of the string

x = "Python is python"
print(x.strip()) #So it will strip all the spaces  towards left or towards rightand give us the result.

#We can also remove one character either starting side or ending side.

print(x.strip('P'))
print(x.strip('n'))
print(x.rstrip("python"))'''

#SPLIT
x = "python is easy"

print(x.split()) #It will convert the string into a list.

print(x.split("is"))
