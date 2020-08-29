import json
import demjson
with open('AllEntries.json', encoding='utf-8') as fh:
    data = json.load(fh)

towrite = open("撩妹.txt",'a',encoding='utf-8') 

# print('data type: '+str(type(data)))
# print('data len: '+str(len(data.keys())))
daydts = data.get('entries')
# print('daydts type: '+str(type(daydts)))
# print('daydts len: '+str(len(daydts))) #与手机端entries保持一致


tagdict =dict()
for oneday in daydts:
    daytags =  oneday.get('tags')
    for tag in daytags:
        if tag not in tagdict.keys():
            tagdict[tag] = 1
        else:
            tagdict[tag] += 1

tagdict= sorted(tagdict.items(), key=lambda d:d[1], reverse = False)
print(tagdict)

    # if(len(daytags)>0 and '撩妹' in daytags):
    #     #print(oneday['tags']) #可以完美的保证覆盖所有撩妹tag的日志
    #     text = (oneday['text'])
    #     # pos = text.find('\n')
    #     # print(text[:pos])
    #     print(text)
    #     print(20*'-')
    #     towrite.write(str(text)+'\n') 
    #     towrite.write(20*'-'+'\n')
# daydts = demjson.decode(json.dumps(data.get('entries')))
# print(daydts)