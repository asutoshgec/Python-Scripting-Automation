x = 67.0

y = 87

print(type(x))
print(type(y))

z = type(x) is type(y)
print(z)

a = [1,2 ,3 ,4 ,5 ,6 ,7 ,8 ]
b = 6 not in a
print(b)

valid_java = ["2.8","1.8"]
host_java = "1.8"
if host_java in valid_java:
    print("The host deployed with valid java version")
else:
    print("The host deployed with invalid java version")
    