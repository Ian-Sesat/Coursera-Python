number=input('Enter a number: ')
try:
    number=int(number)
except:
    number='dollars'
if number== 'dollars':
    print('That is not a number')
else:
    print('Your number is', number)
