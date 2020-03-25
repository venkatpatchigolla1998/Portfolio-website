import json
number=int(input())
result={}
for i in range(number):
    val=input().split(";")
    #print(val)
    if val[0] not in result:
        result.update({val[0]:{"Team":val[0],"Matches Played":0,"Total Points":0,"Won":0,"Tied":0,"Lost":0}})
    if val[1] not in result:
        result.update({val[1]:{"Team":val[1],"Matches Played":0,
        "Total Points":0,"Won":0,"Tied":0 ,"Lost":0}})
#print(result)
    if val[2]=='win':
        result[val[0]]["Matches Played"]+=1
        result[val[1]]['Matches Played']+=1
        result[val[0]]["Total Points"]+=3
        result[val[0]]["Won"]+=1
        result[val[1]]["Total Points"]+=0
        result[val[1]]["Lost"]+=1
    if val[2]=="loss":
        result[val[0]]["Matches Played"]+=1
        result[val[1]]['Matches Played']+=1
        result[val[0]]["Total Points"]+=0
        result[val[0]]["Lost"]+=1
        result[val[1]]["Total Points"]+=3
        result[val[1]]["Won"]+=1
    if val[2]=="draw":
        result[val[0]]["Matches Played"]+=1
        result[val[1]]['Matches Played']+=1
        result[val[0]]["Total Points"]+=1
        result[val[0]]["Tied"]+=1
        result[val[1]]["Total Points"]+=1
        result[val[1]]["Tied"]+=1   
        
result=sorted(result.items())
#result=dict(result)
#print(result)
result=sorted(result,key=lambda x:x[1]['Total Points'],reverse=True)
dct = [v for k,v in result]
#print(dct)
#result=json.dumps(result)
print(json.dumps(dct,indent=4))
