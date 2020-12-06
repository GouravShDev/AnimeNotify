import jsonparser
import animetitle
import constants
from time import sleep
import filehandlers

def collectRelatedMalID(api_path, mal_id):
    # takes api url and a related mal_id as param
    # return list of all related Title objects
    # tested and completed
    # makes request to given mal_id and get releated mal_ids
    # even the mal_id of adaptation (manga)
    sub_url="/anime/%i"%(mal_id)
    #print(api_path+sub_url)
    resp=jsonparser.loadJson(api_path+sub_url)
    related_data=resp['related']
    related_mal_ids=[]

    for datas in related_data:
        for data in related_data[datas]:
            #print(data)
            temp= animetitle.Title(data['type'],data['mal_id'],data['name'])
            related_mal_ids.append(temp)
    return(related_mal_ids)

def collectMalID(api_path, anime_name):
    # api link and name of anime param
    # return topmost malid from results
    # tested and completed
    # search anime and get topmost mal_id from result
    sub_url = "/search/anime?q=%s&page=1"%anime_name
    resp = jsonparser.loadJson(api_path + sub_url)
    mal_id=resp['results'][0]['mal_id']
    mal_name = resp['results'][0]['title']
    print("*****SUBSCRIBE TO******")
    print(mal_name)
    filehandlers.writeRelatedMalID(collectRelatedMalID(api_path, mal_id))
    return(mal_id)

def collectNews(title_type, mal_id):
    # takes MAL id and Type as param
    subUrl = "/{}/{}/news".format(title_type, str(mal_id))
    url = constants.API + subUrl
    resp = jsonparser.loadJson(url)
    for article in resp['articles']:
        sleep(1)
        yield(animetitle.AnimeNews(article['title'], article['intro'], article['url'], article['date']))

#testing
#c=collectNews('anime', 40748)
#for i in c:
#    print(i.title)