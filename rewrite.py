from BestWord import *
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en.examples import sentences
spacyNlp = spacy.load("en_core_web_md")

class ReWrite:
    def __init__(self,sentence, threshold):
        self.sentence = sentence
        self.threshold = threshold


    def write(self):
        wordtypes = ['NN', 'NNS', "NNPS", "NNS", 'JJ', 'JJS']
        tokensentence = spacyNlp(self.sentence)

        newsentence = self.sentence

        rewrite_words = [token.text for token in tokensentence if token.tag_ in wordtypes ]
        for word in rewrite_words:
            newword = BestWord(word, self.threshold).getbestword()
            if newword:
                newsentence = newsentence.replace(word, newword)
        return newsentence




