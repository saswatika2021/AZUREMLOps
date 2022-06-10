from azureml.core import Workspace
from azureml.core.compute import AmlCompute


# Access the workspace from the config.json
ws = Workspace.from_config(path="./config")
cluster_name = "ML-compute-cluster"

# provisioning configuration using Amlcompute
compute_config = AmlCompute.provisioning_configuration(
    vm_size = "STANDARD_D11_V2",
max_nodes=2)

