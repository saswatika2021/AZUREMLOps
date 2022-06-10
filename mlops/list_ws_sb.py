from azureml.core import Workspace,Datastore,Dataset
ws = Workspace.from_config("./config")
ws_list = Workspace.list(subscription_id='458afcdb-91f2-4fc4-b116-fb8d3ef04c0e')
ws_list = list(ws_list)
print(ws_list)
# access default datastore from work place
azure_default_store = ws.get_default_datastore()
# list all the datastores
store_list = list(ws.datastores)
print(store_list)
azure_dataset = Dataset.get_by_name(ws,"adultdata using SDK")

#list datasets from a workspace
ds_list = list(ws.datasets.keys())
for items in ds_list:
    print(items)



