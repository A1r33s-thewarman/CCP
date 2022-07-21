import pandas as pd

df_words = pd.read_csv('datasets/words.csv')

def detector(sentence):
    wrds = list(sentence.split())
    prob = []
    for w in wrds:
        prob.append(str(df_words['tf'].loc[df_words['words'] == w].values[0]))
    return prob


# ret = detector('price ekata shape wenna hondha rasata kaama')
# print(ret)
