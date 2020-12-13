
from json import loads
from requests import get

def jsonParser(dic):
    # takes dict as param
    # dic has json data
    # prints json data
    # tested and completed
    for result in dic["results"]:
        print(result["title"])

def loadJson(url):
    # takes url as param
    # make get request to given url
    # return dict represing json data
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
