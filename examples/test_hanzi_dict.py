from lightdict import HanziDict

hanzi_dic = HanziDict(r'D:\Data\NLP\corpus\words\hanzi.csv')


print('和' in hanzi_dic)
x = hanzi_dic['哈']
print(x)
