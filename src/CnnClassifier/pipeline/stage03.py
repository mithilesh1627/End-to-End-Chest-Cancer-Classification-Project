from CnnClassifier.config.configuration import ConfigurationManger
from CnnClassifier.entity.config_entity import TrainingConfig
from CnnClassifier.components.model_trainer import Training
from CnnClassifier import logger



STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
        obj = TrainingConfig()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e