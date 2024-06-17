import numpy as np
import pandas as pd
import sklearn.cluster as cluster
"""
import umap
import numba

import sklearn.metrics
import vectorizers
import vectorizers.transformers
import sklearn.feature_extractionimport sentence_transformers
impconda install -c conda-forge sentence-transformersort scipy.sparsefrom sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize

import hdbscan
from bertopic import BERTopic
"""
import sentence_transformers
import fastembed
import numpy as np


import hdbscan




#converts a dictionary of pydantic objects to a pandas dataframe
def process_data(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    return df
#embed
def embed_sentences(pydant,  embedding_model):
    """
    model = sentence_transformers.SentenceTransformer(embedding_model)
    embeddings = model.encode(pydant)   
    """
    embeddings: List[np.ndarray] = list(embedding_model.embed(pydant))



    return embeddings   

#run clustering
def run_clustering(embeddings, model, min_cluster_size=3, min_samples=2):
    if model == "HDBSCAN":
        clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples)
        clusterer.fit_predict(embeddings)
        return clusterer
    else:
        return "Invalid model"
    
#main function
def run_model(data):
    model = "HDBSCAN"
    ##embeding_model = "all-mpnet-base-v2"
    df = process_data(data)


    print("beginning embedding")
    embedding_model = fastembed.TextEmbedding()
    embeddings = []
    for index, row in df.iterrows():
        #row[0] = embed_sentences(row[0][1], embedding_model)
        embeddings.append(embed_sentences(row[2][1], embedding_model))
        #row[2] = embed_sentences(row[2][1], embedding_model)
    print("finished embedding")
    
    print(np.shape(embeddings))
    print("beginning clustering")
    titles = df.iloc[:, 1] 
    embeddings = np.array(embeddings).reshape(len(embeddings), -1)
    clusters = run_clustering(embeddings, model)
    print("finished clustering")


        
    cluster_dict = {}
    i = 0
    print(df)
    print(df.keys())
    print(clusters.labels_)    
    labels = clusters.labels_
    num_clusters = clusters.labels_.max() + 1
    for i in range(num_clusters + 2):
        cluster_dict[i] = []
    
    for i in range(len(labels)):
        if labels[i] == -1:
            labels[i] = num_clusters + 1


    i =0
    for index, row in df.iterrows():
        print(row[3][1])
        print(labels[i])
        
        cluster_dict[labels[i]].append(row[3][1])
        i += 1
        
    print(len(cluster_dict))
    return cluster_dict
    

    

 