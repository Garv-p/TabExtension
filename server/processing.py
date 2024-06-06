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

import hdbscan
from bertopic import BERTopic

#converts a dictionary of pydantic objects to a pandas dataframe
def process_data(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    return df
#embed
def embed_sentences(pydant,  embedding_model):
    model = sentence_transformers.SentenceTransformer(embedding_model)
    embeddings = model.encode(pydant)   
    return embeddings   

#run clustering
def run_clustering(embeddings, model, min_cluster_size=3, min_samples=2):
    if model == "HDBSCAN":
        clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples)
        return clusterer.fit_predict(embeddings)
    else:
        return "Invalid model"
    
#main function
def run_model(data):
    model = "HDBSCAN"
    embeding_model = "all-mpnet-base-v2"
    df = process_data(data)
    for column in df.keys:
        item_dict = df[column].dict()
        for keys in item_dict.keys():
            item_dict[keys] = embed_sentences(item_dict[keys], embedding_model=embeding_model)  
        df[column] = pd.Series(item_dict)
    cluster_dict = {}
    for column in df.keys:
        cluster_dict[column] =  1
     
     return cluster_dict
    

    

 