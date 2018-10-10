country = input('where are you from: ')
age = input('how old are you: ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can have driver liscence')
	else:
		print('you can not have driver liscnece')
elif country == 'america':
	if age >= 16:
		print('you can drive')
	else:
		print('you cannot drive')
		