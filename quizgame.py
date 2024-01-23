playing=input('Welcome,do you want to start playing? ')



playing = 'yes'

if playing.lower() != 'yes':
    quit()
print('Let\'s begin')

score=0
answer=input('what is the smallest country in Europe? ')
if answer == 'vatican':
    print("correct")
else:
    print("incorrect")
    score +=1
    
answer=input('what is the biggest country in Europe? ')
if answer == 'russia':
    print("correct")
else:
    print("incorrect")
    score +=1
    
answer=input('which language is spoken in switzerland? ')
if answer == 'french':
    print("correct")
else:
    print("incorrect")
    score +=1    
    
print("you got" +str(score)+" "+"answers correct")