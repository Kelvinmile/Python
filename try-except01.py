astr = 'Hello World'

try:
    istr = int(astr)
except:
    istr = -1

print('First: ', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second: ', istr)