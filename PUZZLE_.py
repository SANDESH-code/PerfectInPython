'''requirment
puzzle game {algorithm}
1.total number of heads = 35
2. total number of legs =94 ,no of rabbit heads(0to 35== head+1)
3.chicken heads=total heads-rabbit heads
4.2 legs = chicken and 4 legs = rabbit,
5. heads =  no of chicks +no of rabbits
6. input
7.output'''
 

#programe
#function
#heads
def solve(heads,legs):#arguments
    for i in range(heads+1): #i=rabbits =(35 heads from 0)
        j=heads- i   ## j = chickens (remaining heads after rabbits)
        #legs
        if 2*j+4*i == legs: #2*chicken+4*rabbit has == legs 
            return j, i
heads = 35   #the given heads 
legs = 94    #the given legs
chickens,rabbits = solve(heads, legs)#function calling
# output
print("no of Chickens are:", chickens)
print("no of Rabbits are:", rabbits)

           


