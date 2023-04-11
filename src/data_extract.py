import os
import pickle
import sys
from src.logger import logging
import pandas as pd
from src.exception import CustomException
from src.datapreprocessor import Preprocessing
from src.model_trainer import Model_Trainer


class DataExtractConfig:
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataExtract:

    def __init__(self):
        self.ingestion_config = DataExtractConfig()

    def data_extract(self):
        try:
            df = pd.read_csv(r'C:\Users\chathuri_105085\PycharmProjects\assignment\data\Language Detection.csv')
            logging.info("reading data completed")
            #print(df.head())
            return df
        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = DataExtract()
    #Extraction of data
    data_input= obj.data_extract()
    logging.info("data is ingested")

    #modifying data
    obj_preprocessor = Preprocessing()
    df_modified = obj_preprocessor.DataSetModifying(data_input)


    #Preprocessing of data
    data_preprocessed = obj_preprocessor.RemoveNonAlphaCharacters(df_modified)
    #data_preprocessed2 = obj_preprocessor.RemoveHTMLElements(data_preprocessed)
    #print(data_preprocessed.head(1000))

    model_trainer = Model_Trainer()
    accuracy = Model_Trainer.bagOfWords_Singlish(data_preprocessed)
    #print(accuracy)

    accuracy = Model_Trainer.randomForestClassifier(data_preprocessed)
    #accuracy= Model_Trainer.bagOfWords_Singlish(data_preprocessed)
    print(accuracy)
