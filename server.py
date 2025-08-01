from flask import Flask, json
from flask import request
from flask_cors import CORS
from googletrans import Translator
# import pathlib
# import random
# import string
# import re
# import numpy as np
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras.layers import TextVectorization
# import pandas as pd
# import numpy as np
# import pickle
translator = Translator()
print(translator.translate('안녕하세요.'))

def custom_standardization(input_string):
    lowercase = tf.strings.lower(input_string)
    return tf.strings.regex_replace(lowercase, "[%s]" % re.escape(strip_chars), "")

from translator import *
from language_identification import detector
from bleu import sentence_bleu

api = Flask(__name__)
CORS(api)


@api.route('/sentence', methods=['POST'])
def get_sentence():
    sentence = request.form.get('sentence')
    # do all things here
    wrds = list(sentence.split())
    detected = detector(sentence)
    detected_ret = dict(zip(wrds, detected))
    sinhala_sen = sentence_translator(sentence)
    sinhala_sen = sinhala_sen.replace('[start]','')
    sinhala_sen = sinhala_sen.replace('[end]','')
    print('=========')
    english_meaning = translator.translate(sinhala_sen)
    ret = [{"id": 1, "sinhala": str(sinhala_sen), "english": str(english_meaning.text), "words": detected_ret}]
    return json.dumps(ret)

@api.route('/scoring', methods=['POST'])
def get_score():
    translated = request.form.get('translated')
    reference = request.form.get('reference')
    # do all things here
    bleu_score = sentence_bleu(reference, translated)
    ret = [{"id": 1, "bleu": str(bleu_score), "sentiment": str(bleu_score)}]
    return json.dumps(ret)

if __name__ == '__main__':
    api.run()
