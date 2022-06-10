from azureml.core import Workspace,Datastore,Dataset
ws = Workspace.from_config("./config")
# Access the Workspace,Datastore,Dataset
azure_store = Datastore.get(ws, "azureml_sdk_blob")
azure_dataset = Dataset.get_by_name(ws,"adultdata using SDK")
azure_default_store = ws.get_default_datastore()
# load the azureml dataset into the pandas dataframe
df = azure_dataset.to_pandas_dataframe()
# upload the dataframe to the azureml dataset

df_sub = df[['AGE','BP','S3']]
Azure_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
    dataframe = df_sub,
    target = azure_store,
    name = "Adult dataset from dataframe"
)

