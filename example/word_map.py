#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""
from os import path
import pickle


from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words

d = path.dirname(__file__)

def difference(data1, data2):
    dict = {}
    for key in data1.keys():
        if key in data2:
            print(data1[key], data2[key])
            value = data1[key] - data2[key]
            dict.update({key: value})
    return dict

text = open(path.join(d, 'sohrab.txt'), encoding='utf-8').read()

# Add another stopword
stopwords = add_stop_words(['شاسوسا'])
# add_stop_words


data_s = pickle.load(open("sohrab_data.pkl", "rb"))
data_m = pickle.load(open("moshiri_data.pkl", "rb"))

frequency_data = difference(data_s, data_m)

# Generate a word cloud image
wordcloud = PersianWordCloud(
    only_persian=True,
    max_words=100,
    stopwords=stopwords,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="black"
).generate_from_frequencies(frequencies=frequency_data)

image = wordcloud.to_image()
image.show()
image.save('difference_word_map.png')
