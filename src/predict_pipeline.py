import sys
import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer

from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass

    def load_object(file_path):
        try:
            with open(file_path, "rb") as file_obj:
                return pickle.load(file_obj)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:

            #model_path = r'C:\Users\chathuri_105085\PycharmProjects\assignment\src\model.pkl'
            model_path = r'C:\Users\chathuri_105085\PycharmProjects\assignment\src\model_logistic.pkl'
            print("Before Loading")
            #model = self.load_object(file_path=model_path)
            with open(model_path, "rb") as file_obj:
                model = pickle.load(file_obj)

            print("After Loading")
            #sentences = [' '.join(words) for words in features['text']]
            # print(inputData)
            #features = sentences
            # print(features)
            print("features")
            print(features)
            #vectorizer = CountVectorizer()
            vectorizer = CountVectorizer()
            processed_features = vectorizer.fit_transform(features).toarray()
            print("processed_features")
            print(processed_features)
            preds = model.predict(processed_features)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 text: str
                 ):

        self.text = text

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "text": [self.text],

            }
            #print("df")
            df =pd.DataFrame(custom_data_input_dict)
            #return pd.DataFrame(custom_data_input_dict)
            print(df['text'])
            return df['text']

        except Exception as e:
            raise CustomException(e, sys)