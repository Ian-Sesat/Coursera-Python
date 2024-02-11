str='X-DSPAM-Confidence: 0.8475'
colonPos=str.find(':')
#print(colonPos)
infoExtracted=str[colonPos+2:]
#print(infoExtracted)
numberExtracted=float(infoExtracted)
print(numberExtracted)