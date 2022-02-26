import re
text = "  This is a pythooooooooooon and it is easy.@_---- to learn_@@@@____@@@@ \n ....@ learn and learn and learn and learn "
#This will match the string, with the given pattern. like is with first "Th", then "is" with "hi", then "is" with "is" like this
my_pat = "is" #This is the pattern
print(len(re.findall(my_pat,text))) #Now if we want to find out the lenth of the patern, like the number of times the pattern is there
print(re.findall(my_pat,text))

#Now I want to search for "is" and "it" in the string, so I need to make a pattern, so that I can search
#"is" "it" here i is common, so I can write i[st]
new_pat = "i[st]"
print(re.findall(new_pat,text))

new_pat1 = r"\bpytho{1,2,4}n\b" #Matches tab, newline, return respectively.
print(re.findall(new_pat1,text))

'''
text = "This is my ip of a db server: 255.100.102.103  234567890987654321"
#Lets say I want to get the IP only
pattern = "^" #here wit this option I am getting all the other numbers also
#If I want to get only the Ip addressthen we have to use "\."
print(re.findall(pattern,text))'''