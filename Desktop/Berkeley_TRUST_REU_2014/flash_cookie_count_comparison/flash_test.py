import re
##
##def filterSites(site):
##    """Filter address strings for consistent abbreviations (uses re module).
##
##       uses regexp to filter out ' AVENUE', ' STREET', ' ROAD', any others?
##       put space in front of search pattern to have more restricted match
##       return the filtered string
##       """
##    addr = re.sub(r' AVENUE', ' AVE', addr)
##    addr = re.sub(r' STREET', ' ST', addr)
##    addr = re.sub(r' ROAD', ' RD', addr)
##    addr = re.sub(r' DRIVE', ' DR', addr)
###    print(addr)
##    return addr

#with open('/Users/Katie/Desktop/sites_test.txt', encoding='utf-8', mode='r') as f:
f = open('/Users/Katie/Desktop/sites_test.txt', 'r', encoding='LATIN-1')
f2 = open('/Users/Katie/Desktop/sites_test2.txt', 'w', encoding='LATIN-1')

# define C as list with 8 elements
newSites = [None]*1

##header = f.readline()
##print(header)
##f2.write(header)

line = f.readline()
#remove whitespace on both ends
site = line.strip()
print site
##storeDataA = line.split('\t')
##storeDataA[1] = storeDataA[1].strip()
##storeDataA[2] = storeDataA[2].strip()
# filter both fields that might have street addresses
##storeDataA[1] = filterAddress(storeDataA[1])
##storeDataA[2] = filterAddress(storeDataA[2])
##
##if len(storeDataA[5])>7:
##    oldZip = storeDataA[5]
##    print(oldZip)
##    newZip = oldZip[:5]
##    

for site in f:
    
    siteB = line.split('\t')
    print siteB
##    storeDataB[1] = storeDataB[1].strip()
##    storeDataB[2] = storeDataB[2].strip()
##    # filter both fields that might have street addresses
##    storeDataB[1] = filterAddress(storeDataB[1])
##    storeDataB[2] = filterAddress(storeDataB[2])
##
##    storeDataB[3] = storeDataB[3].strip()
##    storeDataB[5] = storeDataB[5].strip()

##    if len(storeDataB[5])>7:
##        oldZip = storeDataB[5]
##        #print(oldZip)
##        newZip = oldZip[:5]
##        storeDataB[5] = newZip
    
    # list out store names[0] that have semicolon, zip code[5] first so easier to find
    #if storeDataB[0].find(';')>-1:
    #    print(storeDataB[5],' ',storeDataB[0])

    # if B is dupe of A: same street addr[1], city[3], zip[5] -- assuming same zip means same state
    if site == siteB:
        newSites
        #print(storeDataA)
        for i in range(len(storeDataA)):
            #find which one is longer for each address field
            if len(storeDataA[i])>len(storeDataB[i]):
                storeDataC[i] = storeDataA[i]
            
            else:
                storeDataC[i] = storeDataB[i]
        #becomes new comparison string    
        storeDataA = storeDataC
    
    else:  # not a duplicate so save storeDataA (the old/previous line) and write to file f2
        joinedBack = '\t'.join(storeDataA)
        #print(joinedBack)
        f2.write(joinedBack)
        # move on to next
        storeDataA = storeDataB

f.close()
f2.close()
print('***** All done!  What next?  *****')
