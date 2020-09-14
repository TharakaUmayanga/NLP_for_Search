from rewrite import ReWrite

sentence = "Colombo is the commercial capital and largest city of Sri Lanka by population. According to the Brookings Institution, Colombo metropolitan area has a population of 5.6 million, and 752,993 in the city proper. It is the financial centre of the island and a tourist destination."

print(" Original Sentence {} \n Rewrote sentence {}".format(sentence, ReWrite(sentence, 0.9).write()))


