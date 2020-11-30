import jsonparser

def subscribeAnime(api_path, anime_name):
    # Ask User name of Anime
    # Prepare Url for searching Anime titles
    sub_url = "/search/anime?q=%s/Zero&page=1"%anime_name
    dic = jsonparser.loadJson(api_path + sub_url)
    jsonparser.jsonParser(dic)

def subscribeManga(api_path, manga_name):
    pass

def subscribePerson(api_path, person_name):
    pass

def subscribeStudio(api_path, studio_name):
    pass

def rmSubscribe():
    pass
