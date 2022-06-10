from azureml.core import Workspace,Datastore,Dataset
ws = Workspace.from_config("./config")
# Access the Workspace,Datastore,Dataset
azure_store = Datastore.get(ws, "azureml_sdk_blob")
azure_dataset = Dataset.get_by_name(ws,"adultdata using SDK")
azure_default_store = ws.get_default_datastore()
# load the azureml dataset into the pandas dataframe
df = azure_dataset.to_pandas_dataframe()

# upload local files to storage account using data store
files_list = ['./data/adultincome+first+100.csv']
azure_store.upload_files(files = files_list,
                         target_path= "Adult Data/",
                         relative_root= "./data/",
                         overwrite = True)