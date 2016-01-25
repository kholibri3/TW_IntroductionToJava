#split into array values
#make column A into a list 2009list 0
#column C into a list 2011list 2
#column E into a list 2012list 4
#column G into a list 2014list 6 
#column I into a list alldomains 8
#cross-reference
#go through all domains, one site by one site
#if the domain is in list, depending on which list, look at the column to its right
#paste that number into a new column

#TRUST REU UC Berkeley
#COMPARING FLASH COOKIE COUNTS FROM 2009,2011,2012,2014 --task done manually as well
file = open('/Users/Katie/Desktop/flash_data_python.txt', 'r', encoding='LATIN-1')
file2 = open('/Users/Katie/Desktop/flash_data_python2.txt', 'w', encoding='LATIN-1')

#lists of domains per year
ohnine_list = []
eleven_list = []
twelve_list = []
fourteen_list = []
all_domains = []

#lists of FCC count per year
ohnine_num = []
eleven_num = []
twelve_num = []
fourteen_num = []

#lists to hold new numbers
nine = []
eleven = []
twelve = []
fourteen = []

for line in file:
    splitting = line.split('\t')
    ohnine_list.append(splitting[0].strip())
    ohnine_num.append(splitting[1].strip())
    eleven_list.append(splitting[2].strip())
    eleven_num.append(splitting[3].strip())
    twelve_list.append(splitting[4].strip())
    twelve_num.append(splitting[5].strip())
    fourteen_list.append(splitting[6].strip())
    fourteen_num.append(splitting[7].strip())
    all_domains.append(splitting[8].strip())

#print(ohnine_num)
    
#counters for diff lists nine eleven twelve fourteen
#start at -1 so the first one is 0
n = -1
e = -1
t = -1
f = -1

for site in all_domains:
    if site in ohnine_list:
        n+=1
        #print(site)
        nine.append(ohnine_num[n])
        #print(ohnine_num[x])
        #nine.append('X')
    else:
        nine.append('0')

    #print(nine)
    if site in eleven_list:
        e+=1
        eleven.append(eleven_num[e])
        #eleven.append('X')
    else:
        eleven.append('0')

    #print(eleven)
    
    if site in twelve_list:
        #twelve.append('X')
        t+=1
        twelve.append(twelve_num[t])
    else:
        twelve.append('0')
    #print(twelve)
    if site in fourteen_list:
        #fourteen.append('X')
        f+=1
        fourteen.append(fourteen_num[f])
        #print(fourteen_num[x])
    else:
        fourteen.append('0')
    #print(fourteen)


y = -1
for site in all_domains:
    y+=1
    #print(ohnine_num)
    if(nine[y]=='0' and eleven[y]=='0' and twelve[y]=='0' and fourteen[y]=='0'):
        file2.write('')
        file2.write('\n')
    else:
        joinedBack = str.join('\t', (all_domains[y], nine[y], eleven[y], twelve[y], fourteen[y]))
        file2.write(joinedBack)
        file2.write('\n')
    

file.close()
file2.close()
    
