from CnnClassifier.config.configuration import ConfigurationManger
from CnnClassifier.entity.config_entity import DataIngestionConfig
from CnnClassifier.components.data_ingestion import DataIngestion

from CnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e