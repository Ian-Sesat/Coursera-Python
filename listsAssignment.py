myText=open('mbox-short.txt','r')
for text in myText:
    text=text.rstrip()
    splitText=text.split()
    if len(splitText) <3:
        continue
    if splitText[0] != 'From':
        continue
    #print(splitText)
    print(splitText[2])
