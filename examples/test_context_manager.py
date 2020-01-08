from lightdict import WordDict, HanziDict

hanzi_dic = HanziDict(r'D:\Data\NLP\corpus\words\hanzi.csv', keep=False)

word_dict = WordDict(r'D:\Data\NLP\corpus\words\words.csv', keep=False)

with hanzi_dic:
    print('和' in hanzi_dic)

with word_dict:
    print('开云见日' in word_dict)
