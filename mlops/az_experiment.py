from azureml.core import Workspace,Datastore,Dataset,Experiment
ws = Workspace.from_config("./config")
# Access the Workspace,Datastore,Dataset
azure_store = Datastore.get(ws, "azureml_sdk_blob")
azure_dataset = Dataset.get_by_name(ws,"adultdata using SDK")
azure_default_store = ws.get_default_datastore()
# create/Access an experiment object
experiment = Experiment(workspace=ws,
                        name = "Adult-income-sdk-exp")
#run experiment
new_run = experiment.start_logging()
df = azure_dataset.to_pandas_dataframe()
total_observations = len(df)
nulldf = df.isnull().sum()
# log the matrics to the workspace
new_run.log("Total observations", total_observations)
for columns in df.columns:
    new_run.log(columns,nulldf[columns])

new_run.complete()




