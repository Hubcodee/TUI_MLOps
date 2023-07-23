import sys
import subprocess 
ip = sys.argv[1]


#=============================================================================================================


def run_hadoop_daemon(nn_ip):
    # Configure core-site.xml
    core_site_xml = f"""<?xml version="1.0"?>
    <configuration>
        <property>
            <name>fs.default.name</name>
            <value>hdfs://{nn_ip}:9001</value>
        </property>
    </configuration>"""
    with open("/usr/local/hadoop/conf/core-site.xml", "w") as f:
        f.write(core_site_xml)

    # Configure hdfs-site.xml
    hdfs_site_xml = """<?xml version="1.0"?>
    <configuration>
        <property>
            <name>dfs.name.dir</name>
            <value>/usr/local/hadoop_tmp/hdfs/namenode</value>
        </property>
    </configuration>"""
    with open("/usr/local/hadoop/conf/hdfs-site.xml", "w") as f:
        f.write(hdfs_site_xml)

    # Replace '/path/to/hadoop' with the actual path to your Hadoop installation
    hadoop_home = '/usr/local/hadoop/'
    
    # Replace 'datanode' with the desired Hadoop daemon name, e.g., 'namenode', 'secondarynamenode', etc.
    daemon_name = 'namenode'
    
    # Build the command to start the Hadoop daemon
    command1 = f'{hadoop_home}/bin/hadoop-daemon.sh start {daemon_name}'
    command2 = f'{hadoop_home}/bin/hadoop {daemon_name} -format'
    try:
        # Run the command and capture the output
        process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process2.communicate()
        # Print the output if needed
        print(f'Stdout: {stdout.decode()}')
        print(f'Stderr: {stderr.decode()}')


        if process2.returncode == 0:
            print(f'{daemon_name} formatted successfully.')
        else:
            print(f'Error formatting {daemon_name}.')

        process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process1.communicate()



        # Print the output if needed
        print(f'Stdout: {stdout.decode()}')
        print(f'Stderr: {stderr.decode()}')

        # Check the return code to determine if the command was successful
        if process1.returncode == 0:
            print(f'{daemon_name} started successfully.')
        else:
            print(f'Error starting {daemon_name}.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    run_hadoop_daemon(ip)

