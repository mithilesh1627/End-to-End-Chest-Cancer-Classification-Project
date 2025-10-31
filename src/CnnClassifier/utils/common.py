import os 
from box.exceptions import BoxValueError
import ensure
import yaml
from CnnClassifier import logger
import json , joblib,base64
from ensure import ensure_annotations
from box  import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_of_file:Path)->ConfigBox:

    """Read the YAML file 

    Args:
        file_to_path (Path): path of yaml file

    Returns:
        ConfigBox: ConfigBox
    """
    try:
        with open(path_of_file) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_of_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError() : 
        raise ValueError("yaml file is empty")
    except Exception as e :
         raise e 
    

@ensure_annotations
def create_directories(path_of_file:list,verbose=True):
    """Create the directories

    Args:
        path_of_file (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.
    """

    for path  in path_of_file:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """Save the json data

    Args:
        path (Path): _description_
        data (dict): _description_
    """
    with open(path,'w') as file:
        json.dump(data,file,indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json file data 

    Args:
        path (Path): _description_

    Returns:
        ConfigBox: _description_
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)
    
@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """

    joblib.dump(data,filename=path)
    logger.info(f"binary file saved at : {path}")


@ensure_annotations
def laod_bin(path:Path)->Any:
     """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
     data = joblib.load(path)
     logger.info(f"binary file loaded from : {path}")
     return data


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring,filename) -> None:
    imgdata = base64.b64decode(imgstring)
    with open(filename,'wb') as f :
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath)  -> bytes:
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())