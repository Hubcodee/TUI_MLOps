#! /bin/bash

systemctl start firewalld

firewall-cmd --zone=public  --add-masquerade --permanent

firewall-cmd --zone=public  --add-port=9001/tcp --permanent

firewall-cmd --zone=public  --add-port=50070/tcp --permanent

firewall-cmd --reload 

systemctl restart docker
