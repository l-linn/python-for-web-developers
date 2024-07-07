my_file = open('desserts.txt','r')
#print(my_file.read())
print(my_file.read(20))
print(my_file.tell())
my_file.close()

my_file = open ('hello.txt','w')
my_file.write('hello!')
my_file.close()
