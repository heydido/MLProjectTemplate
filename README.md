# MLProjectTemplate
A Data Science project template with MLOps frameworks

## Setting Up the Project using this template:
1. Click on `Use this template` -> `create a new repository`
2. Put your repository name and description -> `create repository`
3. Clone the repository to your local machine 
4. Rename/Update:
   1. `template.py`: update the project name and add more files/folders [Optional]
   2. the project folder `(src/MLProjectTemplate)` to `(src/YourProjectName)`
   3. README
   4. `requirements.txt` with your project dependencies
   5. `setup.py` with your/your project details
5. Create a virtual environment using setup.sh:
    ```
    bash setup.sh 
    ```
6. Activate the virtual environment (optional, if not done in step 6):
    ```
    source activate ./venv
    ``` 
----
## Workflow:
1. Update config: `config/config.yaml`
2. Update raw/processed data schema: `raw_schema.yaml/processed_schema.yaml` (if needed)
3. Update model parameters: `params.yaml` (if needed)
4. Update the entity: `src/MlProjectTemplate/entity/config_entity.py`
5. Update the configuration manager: `src/MlProjectTemplate/config/configuration.py`
6. Update the components: `src/MlProjectTemplate/components`
7. Update the pipeline: `src/MlProjectTemplate/pipeline`
8. Update entry point: `main.py`
9. Update application: `app.py`

---
## Project Organization:
```
|── .dvc                                              <- dvc cache, config, remote info
|── .github                                           <- ci/cd workflows
|── artifacts                                         <- o/p of pipelines that are needed for execution of next pipelines
|── config                                            <- configurations for all the components of the project
|── docs                                              <- documentation of the project src code
|── logs                                              <- log file generated while running the component/s
|── mlruns                                            <- MLFlow: all ml experiments and their artifacts 
|── notebooks                                         <- jupyter-notebooks
|    |__ data                                         <- sample data to do experiments in the notebook
|
|── references                                        <- quick reference for the project. e.g. research papers
|── reports                                           <- reports generated in the project life-cycle
|	|__ figures
|
|── scripts                                           <- shell scripts to invoke operations from the command line. e.g. run all tests
|── src
|    |__ ProjectName
|        |── __init__.py
|        |── logger.py                                <- A custom logger to stream logs in a terminal/log in file
|        |── exception.py 							  <- A custom exception handler for the project
|        |── components                               <- components of the ml pipeline
|        |    |── __init__.py
|        |    |── data_ingestion.py
|        |    |── data_valaidation.py
|        |    |── data_preprocessing.py
|        |    |── data_transformation.py
|        |    |── model_training.py
|        |    |── model_evaluation.py
|        |    |__ prediction.py
|        |    
|        |── config                                   <- configuration for the component
|        |    |── configration.py
|        |    |__ __init__.py
|		 |
|        |── constants                                <- constants used in the project
|        |    |── __init__.py
|        |        |── PROJECT_ROOT
|        |
|        |── entity                                   < datasclass for each component
|        |    |── __init__.py
|        |    |__ config_entity.py
|        |
|        |── pipeline                                 <- all steps in the pipeline
|        |    |── __init__.py
|        |    |── data_ingestion.py
|        |    |── data_valaidation.py
|        |    |── data_preprocessing.py
|        |    |── data_transformation.py
|        |    |── model_training.py
|        |    |── model_evaluation.py
|        |    |__ predict.py
|        |   
|        |── utils                                    <- all utilities used in the project
|             |── __init__.py
|             |__ common.py							  <- common utilities for the project
|
|── static                                            <- assets/CSS/JS
|── templates                                         <- HTML
|    |── index.html
|    |__ results.html
|
|── tests                                             <- tests for the project
|    |── unit
|    |__ integration
|
|── .dvcignore
|── .gitignore
|── app.py                                            <- expose application via API
|── DockerFile                                        <- containerize the application
|── dvc.yaml                                          <- DVC pipeline
|── LICENSE
|── main.py                                           <- entry point for the project
|── README.md
|── requirements.txt
|── setup.py                                          <- package project 
|── setup.sh                                          <- initial setup for the project
|__ template.py                                       <- creates empty files/folders 
```
---

Owner: [Aashish Kumar](https://www.linktr.ee/heydido)

---
