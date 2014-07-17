f = open('/Users/Katie/Desktop/upper.txt', 'r', encoding='LATIN-1')
f2 = open('/Users/Katie/Desktop/lower.txt', 'w', encoding='LATIN-1')

for row in f:
    allLower = row.lower()
    f2.write(allLower)
    #f2.write('\n')

f.close()
f2.close()




