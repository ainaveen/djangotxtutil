#usage pass a number with the script and get the table as the output
import sys

class math:
    # inputvar =[]
    def __init__(self):
        # validation = len(sys.argv)
        # if validation<=1:
        #     print('Invalid Usaage , expected: mathfn integer. Example "mathfn.py 2" ')
        # else: 
        #     inputvar=sys.argv
        pass
    def getTable(self,num): 
        num=int(num)
        print("********************Start of Program***********************")    
        for i in range(1,11):
            print("%s x %s = %s"%(num,i, num*i))
        print("********************End of Program***********************") 
        return 1 


# math.getTable(sys.argv[1])
