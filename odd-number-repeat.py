#Find the repeatation of the odd numbers given in a string
from collections import Counter
x = "1 2 3 4 5 6 7 8 9 0 7 6 5 4 3 2 1 3 5 7 9 1 3 5 7 "
y = list(x.split())
print(y)
o_l=[]
for i in y:
   if int(i) % 2 != 0:
      o_l.append(i)
print(o_l)
#count repeated elements in the list
c = Counter(o_l)
print(c)