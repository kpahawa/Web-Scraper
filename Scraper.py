__author__ = 'kpahawa'

"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


videoPlayerList = ['videofun.me','play44.net','video44.net','auengine.com','streamingmp4.net']
siteList = ['animeultima.tv', 'animecenter.tv' ]
"""
-http://www.animeultima.tv/ || fairy-tail-episode-100/ <-- the format appears to be anime name (multiple words with dashes) + "episode" + episode_number
-https://www.animecenter.tv/ || watch/hunter-x-hunter-2011--episode-131 <-- similar format but anime name + two dashes. Note the "watch" right after .tv/
"""
url = ''
anime = ''
animeUltimaList = []
class Scraper:
    def __init__(self):
        pass
    def setURL(self,newURL):
        url = newURL
        return url
    def setAnimeName(self, newAnime):
        anime = newAnime
        return anime

    def getHTMLTags(self, url,anime):
################################################
### This section of the code works only for  ###
### Animecenter.tv                           ###
################################################
        # try:
        #     url = "http://www." + siteList[1]
        #     animeURL = url + '/watch/'+anime
        #     r = Request(animeURL,headers={'User-Agent': 'Chrome/35'})
        #     data = urlopen(r).read()
        #     soup = BeautifulSoup(data)
        #
        #     for link in soup.find_all('iframe'):
        #         if videoPlayerList[-1] in link.get('src'):
        #             correctStream = link.get('src')
        #     if correctStream != None:
        #         correctStream.replace('amp','')
        #         #print(correctStream)
        # except:
        #     pass
################################################
### This section of the code works only for  ###
### animeultima.tv                           ###
################################################
        try:
            url = "http://www." + siteList[0]
            animeURL = url + '/'+anime
            r = Request(animeURL,headers={'User-Agent': 'Chrome/35'})
            data = urlopen(r).read()
            soup = BeautifulSoup(data)
            for link in soup.find_all('iframe'):
                if videoPlayerList[-2] in link.get('src'):
                    correctStream = link.get('src')
                    self.setUltimaList(correctStream, anime)
                    return True
        except:
            return False

    def setUltimaList(self,element,anime):
        aList = [element, anime]
        animeUltimaList.append(aList)

    def getUltimaList(self):
        return animeUltimaList
