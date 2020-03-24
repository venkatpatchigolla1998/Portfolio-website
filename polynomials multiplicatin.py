val1=int(input())
dic1={}
dic2={}
result={}
result1={}
for i in range(val1):
    power,coffecient=map(int,input().split(" "))
    dic1[power]=coffecient
#print(dic1)    
val2=int(input())
for i in range(val2):
    power,coffecient=map(int,input().split(" "))
    dic2[power]=coffecient
#print(dic2)    
for i in dic1:
    for j in dic2:
        mul=dic1[i]*dic2[j]
        add=i+j
        #print(add)
        #print(mul,add)
        #result[add]=mul
        if add in result:
            result[add]+=mul
        if add not in result:
            result[add]=mul
for key in result:
    if result[key]!=0:
        result1.update({key:result[key]})
#print(result1)       
result1=sorted(result1.items(),reverse=True)
#print(result1)
result2=[]
#if len(result)==0:
    #print(0)
#else:
for key,value in result1:
        #print(key,value)
    result2.append("{}x^{}".format(value,key))
    result1=(" + ").join(result2)
    result1=result1.replace('x^0','')
    result1=result1.replace("+ -",'- ')
    #result=result.replace(" 0x^","")
    #result1=result1.replace("-",'')
print(result1,end="")
