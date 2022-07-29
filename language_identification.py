import pandas as pd
import enchant

d = enchant.Dict("en_US")

df_words = pd.read_csv('datasets/words.csv')

def new_word(word):
    df_words = pd.read_csv('datasets/words.csv')
    result = d.check(str(word))
    new_row = {'words':str(word), 'tf':result}
    #append row to the dataframe
    df_words = df_words.append(new_row, ignore_index=True)
    df_words.to_csv('datasets/words.csv')
    return result

def detector(sentence):
    df_words = pd.read_csv('datasets/words.csv')
    wrds = list(sentence.split())
    prob = []
    for w in wrds:
        if w in df_words['words']:
            prob.append(str(df_words['tf'].loc[df_words['words'] == w].values[0]))
        else:
            prob.append(new_word(w))
    return prob


# ret = detector('test this')
# print(ret)
