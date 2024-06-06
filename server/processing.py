import numpy as np
import pandas as pd
import sklearn.cluster as cluster

import umap
import numba

import sklearn.metrics
import vectorizers
import vectorizers.transformers
import sklearn.feature_extraction
import scipy.sparse

import sentence_transformers

from sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize

import scipy.sparse as sp
import scipy.linalg as la

#converts a dictionary of pydantic objects to a pandas dataframe
def process_data(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    return df
#embed
def embed_sentences(pydant,  embedding_model):
    model = sentence_transformers.SentenceTransformer(embedding_model)
    embeddings = model.encode(pydant)   
    return embeddings   
    
#main function
def run_model(data):
    model = "Bert"
    df = process_data(data)
    for column in df.keys:
        item_dict = df[column].dict()
        for keys in item_dict.keys():
            item_dict[keys] = embed_sentences(item_dict[keys], model  )
        df[column] = item_dict
    
    

 