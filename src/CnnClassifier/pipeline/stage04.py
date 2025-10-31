from CnnClassifier.config.configuration import ConfigurationManger
from CnnClassifier.entity.config_entity import EvalutionConfig
from CnnClassifier.components.model_evaluation import Evaluation
from CnnClassifier import logger



STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        eval_config = config.get_evalution_config()
        eval = Evaluation(config=eval_config)
        eval.evaluation()
        eval.save_score()
        eval.log_into_mlflow()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e