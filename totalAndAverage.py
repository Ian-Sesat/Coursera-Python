addition=None
n=int(input('How many numbers do you wanna key in? '))
myNumbers=[]
print('Please enter',n,' numbers ')
while n>0:
    number=int(input('Enter your number: '))
    myNumbers.append(number)
    n=n-1
for number in myNumbers:
    if addition == None:
        addition=number
    else:
        addition=addition+number

print('Your sum is', addition)
print('Your average is',int(addition/len(myNumbers)))
