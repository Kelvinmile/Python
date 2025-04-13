sh = input('Enter Hours: ')
sr = input('Enter Rate: ')

try:
    fh = float(sh)
except:
    fh = -1

try:
    fr = float(sr)
except:
    fr = -1

if fh > 40:
    regp = fr*40
    otp = (fh-40)*(fr*1.5)
    xp = regp+otp
else:
    xp = fh*fr

print('Pay: ', xp)