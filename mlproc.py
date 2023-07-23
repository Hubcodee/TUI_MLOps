import subprocess as sp
import sys
import os
from time import sleep

type_name = sys.argv[1]
dataset_name = sys.argv[2]

def launchml(type_name,dataset_name):
    print(f"Launching... {type_name} Container")
    cat = sp.run(["docker", "run","-dit", "--name", f"{type_name}", f"mlcont"])
    if(cat.returncode!=0):
        sp.run(["docker", "rm","-f", f"{type_name}"])
        sleep(1)
        sp.run(["docker", "run","-dit", "--name", f"{type_name}", f"mlcont"])
    else:
        pass
    print("Copy data to container")
    os.system(f"docker cp /tmp/{dataset_name} {type_name}:/app/{dataset_name}")

def mlnode(type_name,filename,dataset_name):
    print(f"Executing {type_name} Model")   
    sp.run(["docker","exec",f"{type_name}","python3",f"{filename}",f"{dataset_name}"])

def get_dataset(dataset_name):
    print("Downloading data set from cluster")
    os.system(f"hadoop fs -get /dataset/{dataset_name} /tmp/{dataset_name}")

ROOT = "/app"
if(type_name=="LR") :    
    print('Setting up docker container for Linear Regression Model')
    filename = f"{ROOT}/linear_regression.py"
    get_dataset(dataset_name)
    sleep(1)
    launchml(type_name,dataset_name)
    print("Docker container setup done!!!")
    mlnode(type_name,filename,dataset_name)
elif(type_name=="LogR"):
    print('Setting up docker container for Logistic Regression Model')
    filename = f"{ROOT}/LogR.py"
    get_dataset(dataset_name)
    sleep(1)
    launchml(type_name,dataset_name)
    print("Docker container setup done!!!")
    mlnode(type_name,filename,dataset_name)
elif(type_name=="NN"):
    print('Setting up docker container for Nueural Network Model')
    filename = f"{ROOT}/NN.py"
    get_dataset(dataset_name)
    sleep(1)
    launchml(type_name,dataset_name)
    print("Docker container setup done!!!")
    mlnode(type_name,filename,dataset_name)
else:
    print("Provide valid arg")    




