from azureml.core import Workspace,Datastore
ws = Workspace.from_config(path = "./config")
azure_store = Datastore.register_azure_blob_container(
    workspace = ws,
    datastore_name = "azureml_sdk_blob",
    account_name= "azuremlstname",
    container_name = "azuremlstcontainerblob",
    account_key = "dpKUrYTXCxjYOydYOtyvrdCH8XZ8VYug4vBRtAvGao/W4h62j7igdTSSA1KtcDJFHWIo8dgBC155+AStk********"



)
