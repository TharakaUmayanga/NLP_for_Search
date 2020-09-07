import spacy
from spacy.vocab import Vocab

spacyNlp = spacy.load("en_core_web_md")


# list_of_words = ['rapper ', 'upcoming ', 'catch']
# apple = spacyNlp.vocab.strings["upcomming"]
# print(apple in spacyNlp.vocab.strings)


def correctword(word):
    wordlst = []
    wordlen = len(word)
    for i in range(2, wordlen):
        wordforward = spacyNlp.vocab.strings[word[i:]]
        wordforward = wordforward in spacyNlp.vocab.strings
        # print("wordforeward is {}  is it true {}".format(word[i:], wordforward))
        wordbackward = spacyNlp.vocab.strings[word[:(i + 1)]]
        wordbackward = wordbackward in spacyNlp.vocab.strings
        # print("wordbackward is {}  is it true {}".format(word[:(i+1)], wordbackward))

        if wordforward:
            wordlst.append(word[i:])

        if wordbackward:
            wordlst.append(word[:(i + 1)])
    # print("word list is ", wordlst)
    return (wordlst, wordlen)


def colarword(tuple):
    lst = tuple[0]
    wordlen = tuple[1]
    tokens = spacyNlp(" ".join(lst))
    reallst = [[wrd.similarity(wrd2), wrd.text, wrd2.text] for wrd in tokens for wrd2 in tokens if
               1 > wrd.similarity(wrd2) > 0.01 and ((len(wrd) + len(wrd2)) == wordlen)]

    print("real list is {} \n sorted list is {}".format(reallst, sorted(reallst, key=lambda x: x[0], reverse=True)))
    if len(reallst) > 0:
        return reallst[0][1:]
    else:
        return ["did not identified"]


hashtag = "travelphotography"
searchWord = colarword(correctword(hashtag))

print("hashtag is #{} \nsearch terms are {}".format(hashtag," ".join(searchWord)))
# print((correctword("upcomingrapper")))
