from flask import Flask, json
from flask import request
import pathlib
import random
import string
import re
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import TextVectorization
import pandas as pd
import numpy as np
import pickle

api = Flask(__name__)

@api.route('/sentence', methods=['POST'])
def get_sentence():
    sentence = request.form.get('sentence')

    # do all things here


    ret = [{"id": 1, "sinhala": str(sentence)}]
    return json.dumps(ret)

if __name__ == '__main__':
    api.run()
