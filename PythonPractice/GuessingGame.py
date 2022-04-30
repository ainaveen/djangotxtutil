import random 
x=random.randint(0,100)
print(x)
cnt=10
while cnt>0:
    guess = int(input("Guess a number between 0 to 100, you have %s chances left : "%(cnt)))
    if guess>x:
        cnt-=1
        print('Number guessed is higher, you have %s tries left'%(cnt))
    elif guess<x:
        cnt-=1
        print('Number guessed is lower , you have %s tries left'%(cnt))  
    else:
        print('You guess it Right!! Number is indeed %s'%(guess))
        cnt=0
print("Game Over")

