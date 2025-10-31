import os
import zipfile
import gdown
from CnnClassifier import logger
from CnnClassifier.utils.common import get_size
from CnnClassifier.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = f"https://drive.google.com/uc?/export=download&id={file_id}"
            gdown.download(url=prefix,output=f"artifacts/data_ingestion/data.zip")

            logger.info(f"Downloaded the data from {dataset_url} into file {zip_download_dir}")
        
        except Exception as e :
            raise e 

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)