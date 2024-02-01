largestNumber=None
n=int(input('How many numbers do you wanna key in? '))
myNumbers=[]
print('Please enter',n,' numbers ')
while n>0:
    number=int(input('Enter your number: '))
    myNumbers.append(number)
    n=n-1
for number in myNumbers:
    if largestNumber is None:
        largestNumber=number
    elif number>largestNumber:
        largestNumber=number

print('Your largest number is',largestNumber)