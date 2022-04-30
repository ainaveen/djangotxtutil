from numpy import random
num_list=[]
for i in range(10):
    x = random.randint(100)
    num_list.append(x)
print('Randomly generated numbers are : ',num_list)    
num_list.sort()
print('Ascending order of the number are : ',num_list)
num_list.sort(reverse=True)
print('Descending order of the number are : ',num_list)
