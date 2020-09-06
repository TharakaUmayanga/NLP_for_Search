from rewrite import ReWrite

sentence = "Sri Lanka, officially the Democratic Socialist Republic of Sri Lanka, is an island country in South Asia, located in the Indian Ocean southwest of the Bay of Bengal and southeast of the Arabian Sea"

print(" Original Sentence {} \n Rewrote sentence {}".format(sentence, ReWrite(sentence, 0.8).write()))

