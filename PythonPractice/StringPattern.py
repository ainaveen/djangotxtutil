print("Start of Code")
for j in range(10):
    for i in range(j):
        print( '*',sep='',end='')
    print('')
for k in range(10):    
    for l in range(10-k):
        print( '*',sep='',end='')
    print('')    
##Space Triangle
for a in range(10):
	for c in range(a):
		print(' ',sep='',end='')
	for b in range(10-a):
		print('*',end='')
	print("")
##Inverted Trangle
for a in reversed(range(10)):
	for c in range(a):
		print(' ',sep='',end='')
	for b in range(10-a):
		print('*',end='')
	print("")
cnt=0
nbr=0
for a in range(101):
    nbr=nbr+cnt
    cnt=a+1
print('Sum of all number till %s is %s' %(a ,nbr))
shortcut = (a*(a+1))/2
print('Above calculation can be done by : n*(n+1)/2 : (%s*%s)/2=%s'%(a,a+1,shortcut))


s= 'hello'
print(s[::-1])
