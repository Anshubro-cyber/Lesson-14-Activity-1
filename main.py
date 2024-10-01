file = open('Abcd.txt','r')
print(file.read())
file.close()

file = open('Abcd.txt','r')
print("\n Read in parts \n")
print(file.read(9))
file.close()

file = open('Abcd.txt','a')
file.write("Hi! I am Akshat and I am 13 years old.")
file.close()