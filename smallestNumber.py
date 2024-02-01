smallestNumber=None
n=int(input('How many numbers do you wanna key in? '))
myNumbers=[]
print('Please enter',n,' numbers ')
while n>0:
    number=int(input('Enter your number: '))
    myNumbers.append(number)
    n=n-1
for number in myNumbers:
    if smallestNumber is None:
        smallestNumber=number
    elif number<smallestNumber:
        smallestNumber=number

print('Your smallest number is',smallestNumber)