rawstr = input('Enter a number: ')

try:
    isval = int(rawstr)
except:
    isval = -1

if(isval > 0 ):
    print('Nice Work')
else:
    print('Not a number')