import csv
import json
from tracemalloc import stop
import urllib.parse
import re
import math

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("research_questionnaire_t.csv", index_col=0)

    single_string = ""
    for word in  df['What motivated you to start a career in BPM?']:
        if isinstance(word, str):
            single_string += word + " "
    
    '''
    tags_set = {}
    for tag_collection in tags:
        if not isinstance(tag_collection, str) and math.isnan(tag_collection):
            continue
        tags_list = tag_collection.split(' ')

        normalized_tags = [item.lower() for item in tags_list]
        for tag in normalized_tags:
            if tag in tags_set:
                tags_set[tag] += 1
            else:
                tags_set[tag] = 1
    '''

    #sorted_keywords = {k: v for k, v in sorted(tags_set.items(), key=lambda item: item[1])}

    #with open('commom_keywords.json', 'w+') as f:
    #    f.write(json.dumps(sorted_keywords))

    # Capitalize all the keywords for better visualization
    #capitalized_keywords = {}
    #for k, v in tags_set.items():
    #    capitalized_keywords[k.title()] = v

    # Create and generate a word cloud image:
    custom_stop_words = ["Business", "Process", "Processes", "area", "BPM"] + list(STOPWORDS)

    #stop_words = [STOPWORDS.add(n) for n in custom_stop_words]
    wordcloud = WordCloud(stopwords=custom_stop_words,
                        background_color="white",
                        prefer_horizontal=0.95,
                        max_words=50,
                        scale=5
                ).generate(single_string)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    #countries = gpd.read_file(
    #           gpd.datasets.get_path("naturalearth_lowres"))
    #countries.head()

if __name__ == "__main__":
    main()
