import spacy
import urllib
import json
from nltk.corpus import wordnet
import requests

spacyNlp = spacy.load("en_core_web_md")


class BestWord:

    def __init__(self, word, threshold=0.9):
        self.word = word
        self.threshold = threshold

    def getdatamuse(self):
        url = "https://api.datamuse.com/words?ml={}".format(self.word)
        response = requests.get(url)
        responsejson = response.json()
        words = [word['word'] for word in responsejson]
        return words

    def getfromnltk(self):
        words = []
        for smword in wordnet.synsets(self.word):
            words = [smw.name() for smw in smword.lemmas()]
        return words

    def getbestword(self):
        bestword = ''
        smwords = self.getdatamuse()
        smwordstokens = [spacyNlp(smword) for smword in smwords]
        original_word_token = spacyNlp(self.word)
        tokenlst = [smv.similarity(original_word_token) for smv in smwordstokens]
        maxscore = max(tokenlst)
        if maxscore >= self.threshold:
            maxscore_index = tokenlst.index(maxscore)
            bestword = smwords[tokenlst.index(maxscore)]
        print("Best word is {} Score is {}".format(bestword,maxscore))
        return bestword


# searchWord = "travel"
#
# simmilar = BestWord(searchWord).getdatamuse()
#
# simmilar2 = BestWord(searchWord).getfromnltk()
#
# bestWord = BestWord(searchWord, threshold=0.5).getbestword()
#
# print("datamuse {} \n NLTK {} \n  best words {}".format(simmilar, simmilar2,bestWord))
#
#
