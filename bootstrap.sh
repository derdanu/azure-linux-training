#/bin/bash
wget -O /tmp/master.tar.gz https://github.com/derdanu/azure-linux-training/archive/master.tar.gz
tar xfvz /tmp/master.tar.gz -C /opt

for i in A B C D E; do for j in 1 3 4 9; do for k in $(seq -w 1 ${j} 9999) ; do cat /opt/azure-linux-training-master/files/ADUMMY >> /opt/azure-linux-training-master/files/${i}${k};done; done; done;

rm /opt/azure-linux-training-master/files/ADUMMY

chmod +x /opt/azure-linux-training-master/checker/checker.py
ln -s /opt/azure-linux-training-master/checker/checker.py /usr/local/bin

echo "####################################################################################" > /etc/motd
echo "# The Training files are located in the /opt/azure-linux-training-master directory #" >> /etc/motd
echo "####################################################################################" >> /etc/motd
echo "" >> /etc/motd
echo "" >> /etc/motd