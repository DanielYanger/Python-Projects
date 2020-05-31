import requests
import json
import os


full_matchlist =[]

#Blue Alliance API v3 Call
parameters = {"accept": "application/json", "X-TBA-Auth-Key": ""}
match_api = requests.get("https://www.thebluealliance.com/api/v3/event/2020txdri/matches/simple",params=parameters)
json_data = match_api.json()

#creating a new file
username = os.getlogin()
f = open(f'C:\\Users\\{username}\\Desktop\\schedule.txt',"w")

#making a sorted list
red1 = []
red2 = []
red3 = []
blue1 = []
blue2 = []
blue3 = []
qual_matches=[]

for i in json_data:
    if i['comp_level']=='qm':
        qual_matches.append(i)

sorted_match_data = sorted(qual_matches,key=lambda x: x['match_number'])

#yeet decided to learn json instead
for i in sorted_match_data:
    if i['comp_level']=='qm':
        match_number = i['match_number']
        for team in i['alliances']['red']['team_keys']:
            f.write("Match "+str(match_number)+","+team[3:]+";")
        for team in i['alliances']['blue']['team_keys']:
            f.write("Match "+str(match_number)+","+team[3:]+";")




#Putting together list of match keys not using JSON because I was lazy to learn JSON
#if match_keys.status_code==200:
    #matches = match_keys.text.split(", \n")
    #for i in matches:
        #Getting the proper match keys
        #start = i.index("\"")
        #end = i.index("\"",start+1)
        #full_matchlist.append(i[start+1:end])
    #for i in full_matchlist:
        #match_info = requests.get("https://www.thebluealliance.com/api/v3/match/"+i+"/simple",params=parameters)
        #print(match_info.status_code)

#else:
    #print("error")






#data2 = json.loads(response)
#print(data2)
#data = response.json()
#print(type(data))
#print(data)
#yeet=matches.split("]")
#for i in yeet:
 #   if "frc" in i or "match_number" in i:
  #      print(i)