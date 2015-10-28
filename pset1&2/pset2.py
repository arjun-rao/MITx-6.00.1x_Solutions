balance = 999999
annualInterestRate = 0.18
mir = annualInterestRate/12.0    
accuracy = 0.000001
lower = balance / 12
upper = (balance * ((1 + (mir)) ** 12)) / 12
mmp = 0.5 * (upper + lower)
pb = balance
for month in range(0,12):
        pb -= mmp
        pb *= (1 + mir)

while abs(pb) > accuracy:
    if pb < 0:
        upper = mmp
    else:
        lower = mmp
    mmp = 0.5 * (upper + lower)
    pb = balance
    for month in range(0,12):
            pb -= mmp
            pb *= (1 + mir)
print "Lowest Payment: " + str(round(mmp,2))

