my_list = ['P', 'Y', 'T', 'H', 'O', 'N', 'I', 'N', 'D', 'O']
my_list.remove('P')

#output ['Y', 'T', 'H', 'O', 'N', 'I', 'N', 'D', 'O']
print(my_list)

my_list.remove('N')
# remove hanya menghapus elemen pertama yang dijumpai
# output : ['P', 'Y', 'T', 'H', 'O', 'N', 'I', 'N', 'D', 'O']

# output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
#output []
print(my_list)