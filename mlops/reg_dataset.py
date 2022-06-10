from azureml.core import Workspace,Datastore,Dataset
# Access the workspace from the config.json
ws = Workspace.from_config(path = "./config")
#access
azure_store = Datastore.get(ws, "azureml_sdk_blob")
csv_path = [(azure_store,"diabetes.csv")]
adultincome_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)
adultincome_dataset = adultincome_dataset.register(workspace = ws,
                                                   name = "adultdata using SDK",
                                                   create_new_version=True)
