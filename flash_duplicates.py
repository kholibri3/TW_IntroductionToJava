#import csv

f = open('/Users/Katie/Desktop/sites_test.txt', 'r', encoding='LATIN-1')
f2 = open('/Users/Katie/Desktop/sites_test2.txt', 'w', encoding='LATIN-1')

#csvwriter = csv.writer(f2)

data = []
noDupe = []

for row in f:
    rowL = row.lower()
    data.append(rowL.strip())
    #print(data)

def remove_duplicates(d):
    #print (list(set(data))
    noDupe = list(set(data))
    #print(noDupe)
    return noDupe

noDupe2 = remove_duplicates(data)
sortedNoDupe = sorted(noDupe2)

'''for entry in noDupe:
    joinedBack = '\n'.join(entry)
    print('hereeee')
    f2.write(joinedBack)
    #print(entry)
    #csvwriter.writerow(entry)'''

#print(noDupe2)
for entry in sortedNoDupe:
    f2.write(entry)
    f2.write('\n')
    #print(entry)
    #csvwriter.writerow(entry)

f.close()
f2.close()
    

##first = data[0]
##follow = data[1]
##print(first)
##new = []
##
##for entry in data:
## #   follow = data[1]
##    print(follow)
##
##    if first == follow:
##        new = first
##
##    else:
##        new = follow
##
##    first = new


    
