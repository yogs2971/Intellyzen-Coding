from itertools import combinations 
count = 0
wt = int(input("enter weight:"))
comb = combinations([1, 5,7,9,11],2) 
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 2
comb = combinations([1, 5,7,9,11],3) 
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 3        
comb = combinations([1, 5,7,9,11],4) 
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 4
comb = combinations([1, 5,7,9,11],5) 
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 5
comb = combinations([1,5,7,9,11],6)
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 6
comb = combinations([1,5,7,9,11],7)
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 7
comb = combinations([1,5,7,9,11],8)
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 8 
comb = combinations([1,5,7,9,11],9)
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 9
comb = combinations([1,5,7,9,11],10)
for i in list(comb): 
    if int(sum(i))== int(wt):
        count = 10     
print(count)
