import spacy
from spacy.vocab import Vocab
from itertools import permutations
from itertools import combinations

spacyNlp = spacy.load("en_core_web_md")


def hashtagextract(hashtag):
    predwords = []
    hashtag = hashtag.strip("#")
    hashlen = len(hashtag)
    hashword = spacyNlp.vocab.strings[hashtag]
    if hashword in spacyNlp.vocab.strings:
        predwords.append(hashtag)
        print("word in")
    else :
        permList = [''.join(l) for i in range(len(hashtag)) for l in combinations(hashtag, i + 1) if len(l)>2]

        for word in permList:
            hashperm = spacyNlp.vocab.strings[word]
            if hashperm in spacyNlp.vocab.strings:
                predwords.append(word)

    return (predwords,hashlen)


def checkcorr(tuple):
    lst = tuple[0]
    wordlen = tuple[1]
    tokens = spacyNlp(" ".join(lst))
    comlst = list(combinations(lst,2))
    # print((comlst))
    spacylst = [spacyNlp(" ".join(x)) for x in comlst]

    reallst = [[wrd[0].similarity(wrd[1]), wrd[0].text, wrd[1].text] for wrd in (spacylst)  if
               1 > wrd[0].similarity(wrd[1]) > 0.01 ]

    print("real list is {} \n sorted list is {}".format(reallst[0:10], sorted(reallst, key=lambda x: x[0], reverse=True)))
    if len(reallst) > 0:
        return reallst[0][1:]
    else:
        return ["did not identified"]






test = checkcorr(hashtagextract("#bestcat"))
