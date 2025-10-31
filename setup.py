import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Chest-Cancer-Classification-using-MLflow-DVC"
AUTHOR_NAME = "Mithilesh"
AUTHOR_USER_NAME = "mithilesh1627"
SRC_REPO = "cnnClassifier"
AUTHOR_MAIL = "mithileshchaurasiya1627@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_MAIL,
    descripton = "Chest Cancer Classification using MLFow and DVC ",
    long_description=long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "tensorflow",
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "mlflow"
    ],
    python_requires=">=3.8",
)