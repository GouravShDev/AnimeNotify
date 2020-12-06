from pickle import dumps, loads, dump, load
from datetime import datetime
import constants
import animetitle

def writeRelatedMalID(title):
    with open(constants.RELATED, 'wb') as related:
        for data in title:
            dump(data, related)

def readRelatedMalID():
    with open(constants.RELATED, 'rb') as related:
        while(True):
            try:
                #print(load(related).type)
                yield(load(related))
            except EOFError:
                pass

def writeLastRunDate():
    with open(constants.DATE, 'wb') as DATE:
        dump(datetime.utcnow(), DATE)

def readLastRunDate():
    with open(constants.DATE, 'rb') as DATE:
        return(load(DATE))