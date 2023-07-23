import docker
import subprocess as sp


client = docker.from_env()

cont = client.containers.list()

filenamedn = "/tmp/hadoopdn_script.py"
filenamenn = "/tmp/hadoopnn_script.py"

def namenode(nn):
    ip_add = nn.attrs['NetworkSettings']['IPAddress']
    sp.run(["docker","exec",f"{nn.name}","python3",f"{filenamenn}",f"{ip_add}"])


def datanode(dn,nn_ip):
    sp.run(["docker","exec",f"{dn.name}","python3",f"{filenamedn}",f"{nn_ip}"])


contnn = client.containers.get("hdfs-namenode")
ip_nn_cont = contnn.attrs['NetworkSettings']['IPAddress']

for c in cont:
    if(c.name=='hdfs-namenode'):
        namenode(c)
        print("Hadoop Name Node Found")
    elif(c.name in ['hdfs-datanode1','hdfs-datanode2']):
        datanode(c,ip_nn_cont)
        print("Hadoop Data Nodes Found")
    




