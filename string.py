#n='andleeb'
#l=len(n)
#for i in range(1,l):
 #   if i % 2==0:
  #      print( n[i] )
        #print('index[',i,']',n[i])
# using through function
def inputstring(str):
    for i in range(1,len(str)):
        if i % 2==0:
            print('index[',i,']',str[i])
str=input('plz enter a string:')
inputstring(str)
