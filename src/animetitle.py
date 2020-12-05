# class for anime containg
# Title 
# Mal_ID
from datetime import datetime

class Title:
    def __init__(self,type,id,name):
        self.type = type
        self.mal_id = id
        self.name = name

class AnimeNews:
    def __init__(self, title, description, link, date):
        self.title = title
        self.description = description
        self.link = link
        self.date=datetime.strptime(date[:-6], '%Y-%m-%dT%H:%M:%S')