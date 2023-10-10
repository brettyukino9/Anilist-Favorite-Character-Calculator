import csv
import json
import os
import webbrowser
from pip._vendor import requests
import sys

# arg 1 = username

chars = []
username = sys.argv[1]
query = '''
query ($name: String!) {
  User(name: $name) {
    ...stuff
  }
}

fragment stuff on User {
  name
  favourites {
    characters1: characters(page:1) {
      nodes {
        name {
          full
        }
      }
    }
    characters2: characters(page:2) {
      nodes {
        name {
          full
        }
      }
    }
    characters3: characters(page:3) {
      nodes {
        name {
          full
        }
      }
    }
    characters4: characters(page:4) {
      nodes {
        name {
          full
        }
      }
    }

  }
}

'''

# Define our query variables and values that will be used in the query request
variables = {
    'name': username
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables}).json()
print(response)

for x in range(1,5) :
    for i in response['data']['User']['favourites']['characters'+str(x)]['nodes']:
        chars.append(i['name']['full'].lower())

map = {}
map2 = {}
with open("character_associations.csv", newline="", encoding='latin1') as csvfile:
    rows = csv.reader(csvfile, delimiter=",", dialect="excel")
    data = []
    for row in rows :
        data.append(row)

print(chars)
tester = "Hitagi Senjougahara"
problemShows = ["gundam", "monogatari", "love live", "jojo", "fate"]
for item in data :
    a = item[0]
    aShow = item[1]
    b = item[2]
    bShow = item[3]
    if(item[4] =="lift") :
        continue
    lift = float(item[4])
    if(aShow == bShow or aShow in bShow or bShow in aShow) :
        continue
    problem = 0
    for show in problemShows :
        if((show in aShow.lower()) and (show in bShow.lower())) :
            problem = 1
            break
    if(problem > 0) :
        continue
    for c in chars :
        if(a.lower() == c) :
            if b in map :
                map[b] = map[b] + lift
                if(b == tester) :
                    print("added " +str(lift)+" from "+a)
            elif b.lower() not in chars: 
                map[b] = lift
                if(b == tester) :
                    print("added " +str(lift)+" from "+a)
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
                    print("added " +str(lift)+" from "+b)
            elif a.lower() not in chars: 
                map[a] = lift
                if(a == tester) :
                    print("added " +str(lift)+" from "+b)
            if (lift > 3):
                if a in map2 :
                    map2[a] = map2[a] + 1
                    if(a == tester) :
                        print("strong association from "+b)
                elif a.lower() not in chars: 
                    map2[a] = 1
                    if(a == tester) :
                        print("strong association from "+b)

res = {key: val for key, val in sorted(map.items(), key = lambda ele: ele[1], reverse = True)}
[print(key,':',value) for key, value in res.items()]
res2 = {key: val for key, val in sorted(map2.items(), key = lambda ele: ele[1], reverse = True)}
[print(key,':',value) for key, value in res2.items()]
with open('Results/'+username+' results.txt', 'w', encoding='utf8') as f:
    f.write("Aggregate association between "+username+"'s favorites list and x character\n")
    f.write("-----------------------------------------------------------------------\n")
    for key, value in res.items() :
        f.write(key+' : '+str(value)+"\n")
    f.write("\n\n\n\n")
    f.write("Number of strong associations found between "+username+"'s favorites list and x character\n")
    f.write("-----------------------------------------------------------------------\n")
    for key, value in res2.items() :
        f.write(key+' : '+str(value)+"\n")

