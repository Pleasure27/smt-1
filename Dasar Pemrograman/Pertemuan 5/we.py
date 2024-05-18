from os import path 
 
if path.isfile('values.txt'):
	with open('values.txt', 'r') as file: 
		values = file.read().split('\n') 
else:
	values = [] 
	while True: 
		answer = input('Please enter a value: ') 
		if not answer: 
			break 
		values.append(answer)
	with open('values.txt', 'w') as file: 
		file.write('\n'.join(values))