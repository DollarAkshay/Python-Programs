import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import pickle
from collections import Counter

lemmatizer = WordNetLemmatizer()
lines = 1000000

def create_lexicon(pos, neg):
    lexicon = []
    
    for file in [pos, neg]:
        with open(file, 'r') as f:
            content = f.readlines()
            for line in content:
                words = word_tokenize(line.lower())
                lexicon += list(words)


    lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
    word_dict = Counter(lexicon)

    l2 = []

    for word in word_dict:
        if 50 < word_dict[word] < 1000 :
            l2.append(word)

    print("Lexicon Length :", len(l2))

    return l2


def sample_handling(sample, lexicon, classification):


    featureset = []

    with open(sample, 'r') as f:
        contents = f.readlines()
        for line in contents :
            words = word_tokenize(line.lower())
            words = [lemmatizer.lemmatize(i) for i in words]
            features = np.zeros(len(lexicon))
            for w in words:
                if w in lexicon:
                    idx = lexicon.index(w.lower())
                    features[idx] += 1
            
            features = list(features)
            featureset.append([features, classification])

    return featureset


def create_featuresets_and_labels(pos, neg, test_size=0.1):
    
    lexicon = create_lexicon(pos, neg)
    features = []
    features += sample_handling(pos, lexicon, [1,0])
    features += sample_handling(neg, lexicon, [0,1])
    random.shuffle(features)

    features = np.array(features)

    testing_size = int(test_size*len(features))

    train_x = list( features[:,0][:-testing_size] )
    train_y = list( features[:,1][:-testing_size] )

    test_x = list( features[:,0][-testing_size:] )
    test_y = list( features[:,1][-testing_size:] )

    return train_x, train_y, test_x, test_y


if __name__ == '__main__':
    train_x, train_y, test_x, test_y = create_featuresets_and_labels('Neural Networks/pos.txt', 'Neural Networks/neg.txt') 
    with open('Neural Networks/sentiment.pickle', 'wb') as f:
        pickle.dump([train_x, train_y, test_x, test_y], f)