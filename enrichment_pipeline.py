# enrichment_pipeline.py

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
from sklearn.pipeline import Pipeline

class Matcher(BaseEstimator, TransformerMixin):
    def __init__(self, df, n_candidates=10):
        self.df = df
        self.n_candidates = n_candidates
        self.vectorizer = TfidfVectorizer()
        self.norm_item_vectors = None
        self.nbrs = None
    
    def fit(self, X, y=None):
        self.norm_item_vectors = self.vectorizer.fit_transform(self.df['norm_item'])
        self.nbrs = NearestNeighbors(n_neighbors=self.n_candidates, metric='cosine').fit(self.norm_item_vectors)
        return self
    
    def transform(self, X, y=None):
        matched_items = []
        match_percentages = []
        
        for item in X['item']:
            match, score = self.get_best_match(item)
            matched_items.append(match)
            match_percentages.append(score)
        
        X['norm_item'] = matched_items
        X['matchpercentage'] = match_percentages
        return X
    
    def get_best_match(self, item):
        item_vector = self.vectorizer.transform([item])
        distances, indices = self.nbrs.kneighbors(item_vector)
        candidates = self.df.iloc[indices[0]]['norm_item'].tolist()
        
        best_match, best_score = None, 0
        for candidate in candidates:
            score = fuzz.ratio(item, candidate)
            if score > best_score:
                best_match, best_score = candidate, score
        
        return best_match, best_score

class Merger(BaseEstimator, TransformerMixin):
    def __init__(self, df):
        self.df = df
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        self.df = self.df.drop_duplicates(subset=['norm_item'])
        merged = pd.merge(X, self.df, on='norm_item', how='left', suffixes=('', '_duplicate'))
        return merged.loc[:,~merged.columns.str.endswith('_duplicate')]

class Rounder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['matchpercentage'] = X['matchpercentage'].round(2)
        return X

def enrich_orders_details(orders_details, food_df):
    pipeline = Pipeline([
        ('matcher', Matcher(food_df)),
        ('merger', Merger(food_df)),
        ('rounder', Rounder())
    ])

    enriched_ordersdetails = pipeline.fit_transform(orders_details)
    return enriched_ordersdetails
