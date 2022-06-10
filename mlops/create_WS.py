
from azureml.core import Workspace
ws = Workspace.create(name='Azureml-SDK-WS',
               subscription_id='458afcdb-91f2-4fc4-b116-fb8d3ef04c0e',
               resource_group='Azureml-sdk-RG',
               create_resource_group=True,
               location='eastus2'
               )
ws.write_config(path = "./config")