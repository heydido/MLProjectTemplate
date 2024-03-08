# MLProjectTemplate
A resuable template for Machine Learning projects

## Setting Up the Project using this template:
1. Clone the repository
2. Create a virtual environment using setup.sh:
    ```
    bash setup.sh 
    ```
3. Activate the virtual environment (optional, if not done in step 2)
    ```
    source activate ./venv
    ``` 

## DVC Commands:
1. In a repository, initialize DVC:
    ```
    dvc init
    ```
2. Add data to DVC:
    ```
    dvc add <path to data>
    ```
3. Add data to a remote storage - the config is written in `.dvc/config` file:
    ```
    dvc remote add -d <remote name> <remote path>
    ```
4. Reproduce pipeline:
   ```
   dvc repro
   ```       
5. Push data to remote storage:
    ```
    dvc push
    ```
