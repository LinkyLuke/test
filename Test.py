print('What is your name')
name = input()
if name.upper() == 'LUKE' or 'DAN':
	print('Hi {}'.format(name))
	print('What is your age')
	age = input()
	if age == 24:
		print('Hah you old as fuck')
	elif age == 23:
		print('Decent, decent')
	else: 
		print('YOU LIE')
else:
	print('Fuck off')
input()