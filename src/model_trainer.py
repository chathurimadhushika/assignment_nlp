import pickle

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import f1_score

class Model_Trainer:

    ##get the logistic regression  for classification
    def bagOfWords_Singlish(inputData):
        print("Inside BoW")
        sentences = [' '.join(words) for words in inputData['Text']]
        labelList = inputData['Language']
        vectorizer = CountVectorizer()
        XMatrix = vectorizer.fit_transform(sentences)
        #print (XMatrix)
        X = XMatrix.toarray()
        Y = np.array(labelList)

        clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')

        clf.fit(X, Y)
        with open("model_logistic.pkl",
                  "wb") as file:  # file is a variable for storing the newly created file, it can be anything.
            pickle.dump(clf, file)
        # return accuracy
        accuracy = clf.score(X, Y)
        return accuracy
        # print (clf.score(X, Y))

    def randomForestClassifier(inputData):
        print("inside the random forest classifier")
        sentences = [' '.join(words) for words in inputData['Text']]
        # print(inputData)
        features = sentences
        # print(features)
        labels = inputData.iloc[:, 1].values
        #print(labels)
        vectorizer = CountVectorizer(max_features=2500, min_df=7, max_df=0.8)
        #vectorizer = CountVectorizer()
        processed_features = vectorizer.fit_transform(features).toarray()
        print("processed_features")
        print(processed_features[1])
        X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.2, random_state=0)
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        model=text_classifier.fit(X_train, y_train)
        with open("model.pkl",
                  "wb") as file:  # file is a variable for storing the newly created file, it can be anything.
            pickle.dump(model, file)
        predictions = text_classifier.predict(X_test)
        print("Random FOrest Classifeir Matrics")
        print(confusion_matrix(y_test, predictions))
        print(classification_report(y_test, predictions))
        print(accuracy_score(y_test, predictions))