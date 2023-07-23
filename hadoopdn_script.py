import subprocess 
import sys
# import os
nn_ip = sys.argv[1]

# def datanode_conf(ip):


# #=============================================================================================================
#     os.chdir("/usr/local/hadoop/bin/")
#     # Run DN Daemon
#     sp.run(["./startdn.sh"])
#     print(os.getcwd())

#     # Print the Installation message
#     print("Hadoop DataNode 1.2.1 installation and configuration completed.")

# datanode_conf(ip=nn_ip)


def run_hadoop_daemon(ip):
    # Configure core-site.xml
    core_site_xml = f"""<?xml version="1.0"?>
    <configuration>
        <property>
            <name>fs.default.name</name>
            <value>hdfs://{ip}:9001</value>
        </property>
    </configuration>"""
    with open("/usr/local/hadoop/conf/core-site.xml", "w") as f:
        f.write(core_site_xml)

    # Replace '/path/to/hadoop' with the actual path to your Hadoop installation
    hadoop_home = '/usr/local/hadoop/'
    
    # Replace 'datanode' with the desired Hadoop daemon name, e.g., 'namenode', 'secondarynamenode', etc.
    daemon_name = 'datanode'
    
    # Build the command to start the Hadoop daemon
    command = f'{hadoop_home}/bin/hadoop-daemon.sh start {daemon_name}'
    
    try:
        # Run the command and capture the output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Print the output if needed
        print(f'Stdout: {stdout.decode()}')
        print(f'Stderr: {stderr.decode()}')

        # Check the return code to determine if the command was successful
        if process.returncode == 0:
            print(f'{daemon_name} started successfully.')
        else:
            print(f'Error starting {daemon_name}.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    run_hadoop_daemon(ip=nn_ip)
