from azureml.core import Workspace,Experiment,ScriptRunConfig
ws = Workspace.from_config("./config")
new_experiment = Experiment(workspace = ws,
                            name = "Income_script")
script_config = ScriptRunConfig(source_directory=".",
                                script="180 - Script To Run.py")
new_run = new_experiment.submit(config=script_config)

