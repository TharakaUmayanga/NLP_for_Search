import spacy
from spacy.vocab import Vocab
''' this is testing ground for three or more hashtags'''
spacyNlp = spacy.load("en_core_web_md")


def correctword(word):
    word = word.strip("#")
    wordlst = []
    wordlen = len(word)
    for i in range(2, wordlen):
        wordforward = spacyNlp.vocab.strings[word[i:]]
        wordforward = wordforward in spacyNlp.vocab.strings
        # print("wordforeward is {}  is it true {}".format(word[i:], wordforward))
        wordbackward = spacyNlp.vocab.strings[word[:(i + 1)]]
        wordbackward = wordbackward in spacyNlp.vocab.strings
        # print("wordbackward is {}  is it true {}".format(word[:(i+1)], wordbackward))
        wordmiddle = spacyNlp.vocab.strings[word[i:-i:1]]
        wordmiddle = wordmiddle in spacyNlp.vocab.strings

        if wordforward:
            wordlst.append(word[i:])

        if wordbackward:
            wordlst.append(word[:(i + 1)])

        if wordmiddle:
            wordlst.append(word[i:-i:1])
    # print("word list is ", wordlst)
    return (wordlst, wordlen)


def colarword(tuple):
    lst = tuple[0]
    wordlen = tuple[1]
    tokens = spacyNlp(" ".join(lst))
    reallst = [[wrd.similarity(wrd2), wrd.text, wrd2.text] for wrd in tokens for wrd2 in tokens if
               1 > wrd.similarity(wrd2) > 0.01 and ((len(wrd) + len(wrd2)) == wordlen)]

    # print("real list is {} \n sorted list is {}".format(reallst, sorted(reallst, key=lambda x: x[0], reverse=True)))
    if len(reallst) > 0:
        return reallst[0][1:]
    else:
        return ["did not identified"]


# hashtag = "#travelphotography2019"
# searchWord = colarword(correctword(hashtag))
# hashtags = correctword(hashtag)
# print("hashtag is {} \nsearch terms are {}".format(hashtag," ".join(searchWord)))
# print((correctword("upcomingrapper")))
