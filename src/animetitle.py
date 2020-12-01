# class for anime containg
# Title 
# Mal_ID

class Title:
    def __init__(self,type,id,name):
        self.type = type
        self.mal_id = id
        self.name = name

class AnimeNews:
    def __init__(self,title,description,link):
        self.title = title
        self.description = description
        self.link = link