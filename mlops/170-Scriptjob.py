from azureml.core import Workspace,Experiment,Run,ScriptRunConfig
ws = Workspace.from_config("./config")

experiment = Experiment(workspace=ws,
                        name = "Incom_Script")
#run experiment
script_config = ScriptRunConfig(source_directory = ".",
                                script = "180-ScriptToRun.py")
new_run = experiment.submit(config=script_config)


