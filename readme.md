TURN OFF SE-LINUX

1. RUN FIRST host_script.py 
This script sets firewall permissions for hadoop.

2. RUN pyscript.py
This is intended to install docker in host system and launch containers 
 - hdfs-namenode  exposed port 50070,9001
 - hdfs-datanode 

3. RUN dock_py.py
This aims at executing hadoopdn, hadoopnn scripts in containers respectively
 - hadoopdn_script.py - contains config file and adds ip address of namenode to conf file.
 - starts namenode and datanode daemon

docker run -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts

docker exec containername python3 /app/{}

jenkins -> ML container -> 