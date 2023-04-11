import re
import string
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from bs4 import BeautifulSoup
class Preprocessing():



    punctuation = ["\'", "$", "-", "+", "#", ">", "{", "}", "_", "*", "`", "\\", ":", ";", "!", ",", ".", "...", "..",
                   "?", "....", ")", "(", "-"]

    def RemoveNonAlphaCharacters(self,data_input):
        try:
            logging.info("removing non alpha characters initiated")
            regex = re.compile('[%s]' % re.escape(string.punctuation))
            cleanedList = []

            for i in range(len(data_input)):
                currentPhrase = data_input['Text'].values[i]
                #print(currentPhrase)
                tokenizedList = []
                punctualtionSplittedList = []

                for splitPhrase in currentPhrase.split():
                    #print(splitPhrase)
                    splitPhrase = re.sub('\@\w+', '', splitPhrase)
                    splitPhrase = re.sub('\#\w+', '', splitPhrase)
                    splitPhrase = re.sub('\#', '', splitPhrase)
                    splitPhrase = re.sub('RT', '', splitPhrase)
                    splitPhrase = re.sub('&amp;', '', splitPhrase)
                    splitPhrase = re.sub('[0-9]+', '', splitPhrase)
                    splitPhrase = re.sub('//t.co/\w+', '', splitPhrase)
                    splitPhrase = re.sub('w//', '', splitPhrase)
                    splitPhrase = splitPhrase.lower()
                    tokenizedList.append(splitPhrase.split())

                for tokenizedElem in tokenizedList:
                    punctuation_Removed_Elem = regex.sub('', str(tokenizedElem))
                    punctualtionSplittedList.append(punctuation_Removed_Elem)
                    #print(punctualtionSplittedList)

                data_input['Text'].values[i] = punctualtionSplittedList
                #print(data_input)
            logging.info("removing non alpha characters completed")

            return data_input

        except Exception as e :
            raise CustomException(e,sys)


    def RemoveHTMLElements(self,data_input):
        try:
            logging.info("removing HTML tags initiated")
            for i in range(len(data_input)):
                currentPhase = data_input['Text'].values[i]
                #currentPhase=currentPhase.apply(str)
                #print(currentPhase)
                #currentPhase= re.sub('[^a-zA-Z]', '', str(currentPhase))
                #data_input['Text'].values[i]=BeautifulSoup(currentPhase,"html.parser").get_text()
                #data_input['Text'].values[i] = BeautifulSoup(currentPhase, "html.parser").get_text()
            return data_input
        except Exception as e :
            raise CustomException(e, sys)


    def DataSetModifying(self,data_input):
        try:
            #print(data_input.head())
            logging.info("data set modifying initiated")
            #print(data_input['Language'].value_counts())
            data_input['Language'] = data_input['Language'].apply(lambda x: '1' if x == 'Italian' else '0')
            #print(data_input['Language_N'].value_counts())
            #data_input.drop(columns =['Language'])
            #print(data_input.head(5))
            return data_input
        except:
            pass