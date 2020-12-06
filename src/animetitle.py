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
    def rmPunctuation(self):
        # initializing punctuations string  
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          # Removing punctuations in string 
        # Using loop + punctuation string 
        for ele in self.description:  
            if ele in punc:  
                self.description = self.description.replace(ele, "")
        for ele in self.title:  
            if ele in punc:
                self.title = self.title.replace(ele, "")