#! /bin/bash

yum install java-1.8.0-openjdk-devel -y

wget http://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1.tar.gz

tar -xzvf hadoop-1.2.1.tar.gz

mv hadoop-1.2.1 /usr/local/hadoop

echo 'export HADOOP_PREFIX=/usr/local/hadoop' >> ~/.bashrc 
echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0' >> ~/.bashrc 
echo 'export PATH=$PATH:$HADOOP_PREFIX/bin' >> ~/.bashrc 
echo 'export PATH=$PATH:$HADOOP_PREFIX/sbin' >> ~/.bashrc 
echo 'export PATH=$PATH:$JAVA_HOME' >> ~/.bashrc 
source /root/.bashrc

mkdir -p /usr/local/hadoop_tmp/hdfs/namenode 
mkdir -p /usr/local/hadoop_tmp/hdfs/datanode

chown -R $USER:$USER /usr/local/hadoop_tmp 

cp /usr/local/hadoop/conf/core-site.xml /usr/local/hadoop/conf/core-site.xml.backup  
cp /usr/local/hadoop/conf/hdfs-site.xml /usr/local/hadoop/conf/hdfs-site.xml.backup
