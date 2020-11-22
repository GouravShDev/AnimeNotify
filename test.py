from requests import get
# Library to make get Request
from json import loads

def loadJson(url):
    # Using request's get method to get data
    try:
        response = get(url)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)
    if(response.status_code == 200):
        return loads(response.content)
    else:
        print("Error: " + str(response.status_code) + " : "+ response.reason)
        exit(1)
 
def collectMalID(api_path, anime_name):
    sub_url = "/search/anime?q=%s/Zero&page=1"%anime_name
    resp = loadJson(api_path + sub_url)
    mal_id=resp['results'][0]['mal_id']
    (mal_id)

def collectRelatedMalID(api_path, mal_id):
    # takes api url and a related mal_id as param
    # return list of all related mal_id
    # tested and completed
    # makes request to given mal_id and get releated mal_ids
    # even the mal_id of adaptation (maga)
    sub_url="/anime/%i"%(mal_id)
    print(api_path+sub_url)
    resp=loadJson(api_path+sub_url)
    related_data=resp['related']
    related_mal_ids=[]
    for datas in related_data:
        for data in related_data[datas]:
            temp={'type': data['type'], 'mal_id': data['mal_id']}
            related_mal_ids.append(temp)
    print(related_mal_ids)

collectRelatedMalID("https://api.jikan.moe/v3", 11741)