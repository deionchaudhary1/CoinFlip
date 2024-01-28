from random import*
def oneTrial ():
    #heads = 1 and tails = 0
  flip1 = randint(0,1)==1
  flip2 = randint(0,1)==1
  flip3 = randint(0,1)==1
  numFlips =3
  while not(flip1 ==True and flip2 == True and flip3 == True):
    flip1 = flip2
    flip2 = flip3
    flip3 = randint(0,1)==1
    #flip3 mimics each of the other flips one by one per while loop thing
    numFlips = numFlips+1
  return numFlips

sum = 0
count = 0
while count<1000:
  sum = sum+oneTrial()
  count +=1
print( sum/count)