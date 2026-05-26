import os
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

#The actual worker class. Has one job — run the ingestion process.
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #gets access to all paths
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') #reading csv into pandas dataframe 
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #Creates the artifacts folder if it doesn't already exist. exist_ok=True means don't throw error if folder already exists.

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            #Saves the raw untouched dataframe as artifacts/data.csv

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            #Splits data 80/20, saves both as separate CSVs.

            logging.info("Ingestion of the data is completed")
            return(
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
            )
            #Hands back both paths so the next pipeline step knows where to find the data.

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)