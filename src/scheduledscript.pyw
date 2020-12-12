import constants
import notification
import filehandlers
import collector
from datetime import datetime
import animetitle

def main():
    constants.init()
    last_run_date=filehandlers.readLastRunDate()
    for malid in filehandlers.readRelatedMalID():
        for article in collector.collectNews(malid.type, malid.mal_id):
            if (article.date > last_run_date):
                article.rmPunctuation()
                notification.genNotification(article.title, article.description, constants.ICON_NAME, article.link)
            else:
                break
    filehandlers.writeLastRunDate()

if (__name__=="__main__"):
    main()
