store = [
	{
		'nama':[],
  		'password':[],
	},
]

def store():
    print('Please place your ideas below, press enter to exit')
    while True:
        idea = input()
        if "quit" in idea or "exit" in idea:
            break
        else:
            yield idea

ideas = [x for x in store()]

with open('cuk.txt', 'a') as fp:
    for idea in ideas:
        fp.write(str(f'{idea}\n'))

f = open("cuk.txt", "r")
print(f.read())
print(len("cuk.txt"))
print(store)