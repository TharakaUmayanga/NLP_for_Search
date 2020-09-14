import json
import requests


class GetData:

    def __init__(self,lst):
        self.lst = lst

    def getwebdata(self):
        sentence = "+".join(self.lst)
        searchurl = "https://api.duckduckgo.com/?q={}&format=json&pretty=1".format(sentence)
        print(searchurl)
        response = requests.get(searchurl)
        responsejson = response.json()
        print(responsejson)
        if responsejson["AbstractText"]:
            about = responsejson["AbstractText"]
        else:
            about = self.getwikipedia()

        return about


    def getwikipedia(self):
        sentence = "%".join(self.lst)
        searchurl = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json".format(sentence)
        response = requests.get(searchurl)
        responsejson = response.json()
        print(responsejson)
        title = responsejson["query"]["search"][0]['title']
        pageid = responsejson["query"]["search"][0]['pageid']
        summaryurl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={}".format(title)
        sresponse = requests.get(summaryurl)
        summaryjson= sresponse.json()
        summary = summaryjson['query']['pages'][str(pageid)]['extract']
        wikiurl = "https://en.wikipedia.org/wiki/{}".format(title)
        return summary, wikiurl



