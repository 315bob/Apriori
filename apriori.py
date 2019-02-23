
support = input('input support:')
confidence = input('input confidence:')
file= raw_input('input transactionFile:')
MulSet =[]
transactionList =[]
f = open(file,'r') 
for line in f.readlines():
    line = line[:-1]
    print line
    transactionList.append(line)
for i in range(len(transactionList)):
    transactionList[i]=transactionList[i].split(',')

merchandise = set()
for i in range(len(transactionList)):
    for j in range(len(transactionList[i])):
        merchandise.add(frozenset([transactionList[i][j]])) 

# get all merchandise and the transactionlist

print('')

def scan(kitemSet, support):

        itemSet = set()
        dataSupport = dict()

        for item in kitemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                        	if item not in dataSupport:
                        		dataSupport[item] = 1
                        	else:
                        		dataSupport[item] += 1
                        	
        for item in dataSupport:
        	if dataSupport[item] >= len(transactionList)*support:
        		itemSet.add(item)

        return itemSet,dataSupport
# scan the transactionlist to get itemset which larger or equal than the minsupport
firstSet,dataSupport= scan(merchandise,support)
# get itemset which only have one item
def sub(item):
    sub_all = []
    for i in range(1, 2**len(item)-1):
        temp = list(bin(i))[2:]
        length = len(temp)
        sub = []
        for j in range(length-1, -1, -1):
            if temp[j] == '1':
                sub.append(item[length-j-1])
        sub_all.append(sub)
    return sub_all
# get sublist of list

def getMulISetAndSupp(support):
    KSet= firstSet
    while(len(KSet) >0):
        tem = set()
        for i in KSet:
        	for j in KSet:
        		if len(i.union(j))==len(i)+1:
        			tem.add(i.union(j))
        KSet,Ksupport= scan(tem,support)
        if len(KSet) !=0:
            MulSet.append(KSet)
            dataSupport.update(Ksupport)
    print dataSupport
#get all itemset which have items more than one and all of the support
def getRules(confidence):
    for i in range(len(MulSet)):
        for item in MulSet[i]:
            for i in sub(list(item)):
                conf =  float(dataSupport[item])/float(dataSupport[frozenset(i)])
                if conf >= confidence:
                    for j in i:
                        l = list(item)
                        l.remove(j)
                        print "rule:"+str(i)+" =>"+str(l)+","+"conf:"+str(conf)
                        print('')        

#get rules which items' confidence larger or equal than minconfidence


getMulISetAndSupp(support)
getRules(confidence)

