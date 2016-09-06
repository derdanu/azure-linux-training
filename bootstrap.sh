#/bin/bash
wget -O /tmp/master.tar.gz https://github.com/derdanu/azure-linux-training/archive/master.tar.gz
tar xfvz /tmp/master.tar.gz -C /opt
for i in $(seq -w 1 9999) ; do cat /opt/azure-linux-training-master/files/ADUMMY > /opt/azure-linux-training-master/files/A${i};done; 
echo "####################################################################################" > /etc/motd
echo "# The Training files are located in the /opt/azure-linux-training-master directory #" >> /etc/motd
echo "####################################################################################" >> /etc/motd
echo "" >> /etc/motd
echo "" >> /etc/motd