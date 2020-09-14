from WordCorrection import correctword, colarword


class HashtagNlp:
    def __init__(self,hashtag):
        self.hashtag = hashtag

    def getalldata(self):
        predwords = correctword(self.hashtag)
        if len(predwords[0]) > 0:
            hashtitle = colarword(predwords)
            if hashtitle[0] != "did not identified":
