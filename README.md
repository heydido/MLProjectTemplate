# MLProjectTemplate
A Data Science project template with MLOps frameworks

## Setting Up the Project using this template:
1. Click on `Use this template` -> `create a new repository`
2. Put your repository name and description -> `create repository`
3. Clone the repository to your local machine 
4. Rename/Update:
   1. `template.py`: update project name, and add more file/folders [Optional]
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
------------------------------------------------------------------------------------------------------------------------
## Workflow:
1. Update config: `config/config.yaml`
2. Update raw/processed data schema: `raw_schema.yaml/processed_schema.yaml` (if needed)
3. Update model parameters: `params.yaml` (if needed)
4. Update the entity: `src/MlProjectTemplate/entity/config_entity.py`
5. Update the configuration manager: `src/MlProjectTemplate/config/configuration.py`
6. Update the components: `src/MlProjectTemplate/components`
7. Update the pipeline: `src/MlProjectTemplate/pipeline`
8. Update entrypoint: `main.py`
9. Update application: `app.py`

------------------------------------------------------------------------------------------------------------------------
