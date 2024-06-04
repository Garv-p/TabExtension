
import numpy as np
import pandas as pd
import sklearn.cluster as cluster


import numba

import sklearn.metrics
import vectorizers
import vectorizers.transformers
import sklearn.feature_extraction
import scipy.sparse
!pip install -U sentence-transformers
import sentence_transformers

from sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize
import hdbscan
from bertopic import BERTopic

def load_data():
    data = pd.read_csv('data.csv')
    return data

def embed_sentences(Dataframe df, string column_name, string embedding model):
    model = sentence_transformers.SentenceTransformer(embedding_model)
    embeddings = model.encode(df[column_name].values)   
    return embeddings   
    

def umap_embeddings(embeddings, n_components=2, n_neighbors=15, min_dist=0.1):
    umap = UMAP(n_components=n_components, n_neighbors=n_neighbors, min_dist=min_dist)
    return umap.fit_transform(embeddings)

def hdbscan_clusters(embeddings, min_cluster_size=15, min_samples=5):
    clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples)
    return clusterer.fit_predict(embeddings)

def bertopic_clusters(embeddings, n_gram_range=(1, 1), stop_words='english', top_n_words=10, nr_topics=None):
    vectorizer = vectorizers.transformers.TfidfVectorizer(ngram_range=n_gram_range, stop_words=stop_words)
    doc_term_matrix = vectorizer.fit_transform(embeddings)
    topic_model = BERTopic(nr_topics=nr_topics)
    topics, _ = topic_model.fit_transform(doc_term_matrix)
    return topics




if __name__ == '__main__':
    data = load_data()
    embeddings = embed_sentences(data, 'text', "all-mpnet-base-v2")
    umap_embeddings = umap_embeddings(embeddings)
    hdbscan_clusters = hdbscan_clusters(umap_embeddings)
    bertopic_clusters = bertopic_clusters(embeddings)
    print(hdbscan_clusters, bertopic_clusters)    
 







