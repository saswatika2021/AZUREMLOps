from azureml.core import Workspace,Experiment,Run,ScriptRunConfig,Environment
from azureml.core.environment import CondaDependencies
ws = Workspace.from_config("./config")

experiment = Experiment(workspace=ws,
                        name = "Training_Script")
#create custom environment
myenv = Environment(name="MyEnvironment")
myenv_dep = CondaDependencies.create(conda_packages=['scikit-learn'])
myenv.python.conda_dependencies = myenv_dep
myenv.register(ws)
#run experiment
script_config = ScriptRunConfig(source_directory = ".",
                                script = "Training-script.py",
                                environment=myenv)
new_run = experiment.submit(config=script_config)
