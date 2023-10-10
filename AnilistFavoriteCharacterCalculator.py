import csv

map = {}
map2 = {}
with open("character_associations.csv", newline="", encoding='latin1') as csvfile:
    rows = csv.reader(csvfile, delimiter=",", dialect="excel")
    data = []
    for row in rows :
        data.append(row)

with open("favorite characters.txt", newline="", encoding='utf8') as csvfile2:
    rows = csv.reader(csvfile2, delimiter=",", dialect="excel")
    chars = []
    for row in rows :
        chars.append(row[0].lower())

print(chars)
count = 0
tester = "Kurapika"
for item in data :
    a = item[0]
    aShow = item[1]
    b = item[2]
    bShow = item[3]
    if(count != 0) :
        lift = float(item[4])
    if(aShow == bShow or aShow in bShow or bShow in aShow or ("monogatari" in aShow.lower() and "monogatari" in bShow.lower())or ("jojo" in aShow.lower() and "jojo" in bShow.lower())) :
        continue
    for c in chars :
        if(a.lower() == c) :
            if b in map :
                map[b] = map[b] + lift
                if(b == tester) :
                    print("added " +str(lift)+"from "+a)
            elif b.lower() not in chars: 
                map[b] = lift
                if(b == tester) :
                    print("added " +str(lift)+"from "+a)
            if(lift > 3) :
                if b in map2 :
                    map2[b] = map2[b] + 1
                    if(b == tester) :
                        print("strong association from "+a)
                elif b.lower() not in chars: 
                    map2[b] = 1
                    if(b == tester) :
                        print("strong association from "+a)
        if(b.lower() == c) :
            if a in map :
                map[a] = map[a] + lift
                if(a == tester) :
                    print("added " +str(lift)+"from "+b)
            elif a.lower() not in chars: 
                map[a] = lift
                if(a == tester) :
                    print("added " +str(lift)+"from "+b)
            if (lift > 3):
                if a in map2 :
                    map2[a] = map2[a] + 1
                    if(a == tester) :
                        print("strong association from "+b)
                elif a.lower() not in chars: 
                    map2[a] = 1
                    if(a == tester) :
                        print("strong association from "+b)
    count = count + 1

res = {key: val for key, val in sorted(map.items(), key = lambda ele: ele[1], reverse = True)}
[print(key,':',value) for key, value in res.items()]
with open('AggregateAssocation.txt', 'w', encoding='utf8') as f:
    for key, value in res.items() :
        f.write(key+' : '+str(value)+"\n")
## COMBINE INTO ONE FILE
res2 = {key: val for key, val in sorted(map2.items(), key = lambda ele: ele[1], reverse = True)}
[print(key,':',value) for key, value in res2.items()]
with open('StrongAssociationCount.txt', 'w', encoding='utf8') as f:
    f.write("number of strong associations found between your list of characters and x character")
    for key, value in res2.items() :
        f.write(key+' : '+str(value)+"\n")