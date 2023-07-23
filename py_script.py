import subprocess

HADOOP = "hadoop_custom"

def install_docker():
    # Install Docker on RHEL 8
    subprocess.run(["sudo", "dnf", "install", "docker-ce", "--nobest", "-y"])
    subprocess.run(["sudo", "systemctl", "start", "docker"])
    subprocess.run(["sudo", "systemctl", "enable", "docker"])

def pull_rhel_image():
    # Pull the RHEL image from Docker Hub
    subprocess.run(["sudo", "docker", "pull", "centos"])

def custom_image()->bool:
    filename = "hadoop-df"
    try:
        subprocess.run(["docker","build","-t",f"{HADOOP}:latest",".", "-f", f"{filename}"])
        print("Build Sucess!!\n")
        return True
    except Exception as e:
        return False
    # print("Image customization success!!")

def launch_container():
    names = ["hdfs-namenode","hdfs-datanode1","hdfs-datanode2"]
    # Launch a Docker container with RHEL image
    for name in names:
        if(name=="hdfs-namenode"):
            print("Launching Name Node")
            subprocess.run(["docker", "run", "-p" ,"9001:9001","-p","50070:50070", "-dit", "--name", "hdfs-namenode", "hadoop_custom"])
            # subprocess.run(["docker", "run", "-p 9001:9001", "-dit","--name", f"{name}", f"{HADOOP}:latest"])
        else: 
            print("Launching DataNode Node")
            subprocess.run(["docker", "run", "-dit", "--name", f"{name}", f"{HADOOP}:latest"])

if __name__ == "__main__":

    # Install Docker on RHEL 8
    #install_docker()

    # Pull RHEL image from Docker Hub
    #pull_rhel_image()

    #Customize Image
    # toLaunch = True
    toLaunch = custom_image()

    # Launch Docker container
    if(toLaunch):
        launch_container()
    else:
        print("Error!!  ")
    # Install and configure Hadoop inside the container
    #install_configure_hadoop()
