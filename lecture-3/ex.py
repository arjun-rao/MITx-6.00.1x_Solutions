#num = 0
#while num <= 5:
#    print num
#    num += 1
#
#print "Outside of loop"
#print num 

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print "Number of apples: " + str(numberOfApples)

num = 10
while num > 3:
    num -= 1
    print num 	
    
    
num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop'

num = 100
while not False:
    if num < 0:
        break
print 'num is: ' + str(num) 

num = 2
while ( num <=10 ):
    print num
    num+=2
print 'Goodbye!'



#myStr = '6.00x'
#
#for char in myStr:
#    print char
#
#print 'done' 


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter

print 'done'


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons) 