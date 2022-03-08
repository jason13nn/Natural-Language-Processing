from myDict import *


# Reading word dict

dfile = open('wlist1')
lines = dfile.readlines()

x = []
for l in lines:
   x.append(l.rstrip())
m = myDict(x)

# read sub file

sfile = open('sub1')
lines = sfile.readlines()

sublist = {}
for l in lines:
    x = l.rstrip().split()
    sublist.update({(x[0], x[1]) : float(x[2])})

# read sub file

sfile = open('sub2')
lines = sfile.readlines()

sublist2 = {}
for l in lines:
    x = l.rstrip().split()
    sublist2.update({(x[0], x[1]) : float(x[2])})

# tfile 

tfile = open('testcase')
lines = tfile.readlines()
for i in range(0, 20):
    x = lines[i].rstrip().split()
    print("Editing Distance (sub = 2) ", x[0], x[1],  editDistance(x[0], x[1]))
    print("Editing Distance (sub = 1) ", x[0], x[1],  editDistance(x[0], x[1], defaultSubCost = 1))
    print("Editing Distance (sublist1) ", x[0], x[1],  editDistance(x[0], x[1], subCostList = sublist))
    print("Editing Distance (sublist2) ", x[0], x[1],  editDistance(x[0], x[1], subCostList = sublist2))
for i in range(20, 25):
    x = lines[i].rstrip().split()
    print("Search (sub = 2)", x[0], m.search(x[0], 5))
    print("Search (sub = 1)", x[0], m.search(x[0], 5, defaultSubCost = 1))
    print("Search (sublist1)", x[0], m.search(x[0], 5, subCostList = sublist))
    print("Search (sublist2)", x[0], m.search(x[0], 5, subCostList = sublist2))

'''
m.print()
m.search("qq", 3)
print(editDistance("ab", "bb"))
print(editDistance("ab", "bb", subCostList ={('a', 'b'): 1}))
print(editDistance("pp", "tpr", subCostList ={('a', 'b'): 3}))
print(editDistance("pp", "tpr", subCostList = sublist))
print(editDistance("pp", "tpr", subCostList = sublist2))
print(m.search('bc', 4))
print(m.search('cct', 4))
'''
