#/bin/bash
wget -O /tmp/master.tar.gz https://github.com/derdanu/azure-linux-training/archive/master.tar.gz
tar xfvz /tmp/master.tar.gz -C /opt
echo "####################################################################################" > /etc/motd
echo "# The Training files are located in the /opt/azure-linux-training-master directory #" >> /etc/motd
echo "####################################################################################" >> /etc/motd
echo "" >> /etc/motd
echo "" >> /etc/motd